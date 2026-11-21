"""
Gerenciador de Tarefas Simples

Aplicativo desenvolvido para demonstrar o uso do GitHub Copilot
em um projeto Python com interface gráfica usando Streamlit.

Autor: Programador Python SR
Data: Agosto 2025
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Protocol, TypedDict, cast

import streamlit as st


class Tarefa(TypedDict):
    """Representa uma tarefa exibida e armazenada na sessão atual."""

    id: int
    nome: str
    concluida: bool


class EstadoTarefasProtocol(Protocol):
    """Define os atributos compartilhados pelo estado real e pelo estado de teste."""

    tarefas: List[Tarefa]
    contador_id: int


@dataclass
class EstadoTarefas:
    """Contêiner de estado que permite testar a lógica sem iniciar o Streamlit."""

    tarefas: List[Tarefa] = field(default_factory=list)
    contador_id: int = 0


def _estado(estado: Optional[EstadoTarefasProtocol] = None) -> EstadoTarefasProtocol:
    """Retorna o estado recebido ou o estado de sessão fornecido pelo Streamlit."""
    if estado is not None:
        return estado
    return cast(EstadoTarefasProtocol, st.session_state)


def inicializar_session_state(
    estado: Optional[EstadoTarefasProtocol] = None,
) -> None:
    """Cria a lista de tarefas e o contador quando ainda não existem no estado."""
    est = _estado(estado)
    if not hasattr(est, "tarefas"):
        est.tarefas = []
    if not hasattr(est, "contador_id"):
        est.contador_id = 0


def adicionar_tarefa(
    nome_tarefa: str, estado: Optional[EstadoTarefasProtocol] = None
) -> bool:
    """Adiciona uma tarefa não vazia e retorna se a operação foi realizada."""
    est = _estado(estado)
    if nome_tarefa.strip():
        nova_tarefa = {
            "id": est.contador_id,
            "nome": nome_tarefa.strip(),
            "concluida": False,
        }
        est.tarefas.append(nova_tarefa)
        est.contador_id += 1
        return True
    return False


def atualizar_status_tarefa(
    tarefa_id: int,
    status: bool,
    estado: Optional[EstadoTarefasProtocol] = None,
) -> None:
    """Atualiza a conclusão da tarefa identificada; não faz nada se não existir."""
    est = _estado(estado)
    for tarefa in est.tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = status
            break


def obter_estatisticas(
    estado: Optional[EstadoTarefasProtocol] = None,
) -> Dict[str, int]:
    """Retorna as quantidades total, concluída e pendente no estado escolhido."""
    est = _estado(estado)
    total = len(est.tarefas)
    concluidas = sum(1 for tarefa in est.tarefas if tarefa["concluida"])
    pendentes = total - concluidas

    return {
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes,
    }


def _adicionar_tarefa_interface() -> None:
    """Processa o envio do formulário e prepara o feedback da interface."""
    nome_tarefa = st.session_state.get("nome_tarefa", "")
    if adicionar_tarefa(nome_tarefa):
        st.session_state["mensagem_sucesso"] = (
            f"✅ Tarefa '{nome_tarefa.strip()}' adicionada com sucesso!"
        )
        st.session_state["mensagem_erro"] = ""
        st.session_state["nome_tarefa"] = ""
    else:
        st.session_state["mensagem_sucesso"] = ""
        st.session_state["mensagem_erro"] = (
            "❌ Por favor, insira um nome válido para a tarefa."
        )


def renderizar_cabecalho() -> None:
    """Exibe o título e as métricas da sessão atual."""
    st.title("📋 Gerenciador de Tarefas")
    st.markdown("---")

    # Exibir estatísticas
    stats = obter_estatisticas()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Tarefas", stats['total'])
    with col2:
        st.metric("Concluídas", stats['concluidas'])
    with col3:
        st.metric("Pendentes", stats['pendentes'])

    st.markdown("---")


def renderizar_formulario_adicionar() -> None:
    """Exibe o campo de texto e o botão para cadastrar uma tarefa."""
    st.subheader("➕ Adicionar Nova Tarefa")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.text_input(
            "Nome da Tarefa",
            placeholder="Digite o nome da tarefa...",
            help="Insira uma descrição clara da tarefa que deseja adicionar",
            key="nome_tarefa",
        )

    with col2:
        st.button(
            "Adicionar",
            type="primary",
            on_click=_adicionar_tarefa_interface,
        )

    if st.session_state.get("mensagem_sucesso"):
        st.success(st.session_state["mensagem_sucesso"])
    if st.session_state.get("mensagem_erro"):
        st.error(st.session_state["mensagem_erro"])


def renderizar_lista_tarefas() -> None:
    """Exibe tarefas, filtros e checkboxes para atualizar seus status."""
    st.subheader("📝 Lista de Tarefas")

    if not st.session_state.tarefas:
        st.info("🎯 Nenhuma tarefa cadastrada ainda. Adicione sua primeira tarefa acima!")
        return

    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        filtro = st.selectbox(
            "Filtrar tarefas:",
            ["Todas", "Pendentes", "Concluídas"]
        )
    
    with col2:
        ordenar_por = st.selectbox(
            "Ordenar por:",
            ["Mais recentes", "Mais antigas", "Concluídas primeiro", "Pendentes primeiro"]
        )

    # Aplicar filtros
    tarefas_filtradas = list(st.session_state.tarefas)

    if filtro == "Pendentes":
        tarefas_filtradas = [t for t in tarefas_filtradas if not t["concluida"]]
    elif filtro == "Concluídas":
        tarefas_filtradas = [t for t in tarefas_filtradas if t["concluida"]]

    # Aplicar ordenação
    if ordenar_por == "Mais antigas":
        tarefas_filtradas.sort(key=lambda x: x["id"])
    elif ordenar_por == "Mais recentes":
        tarefas_filtradas.sort(key=lambda x: x["id"], reverse=True)
    elif ordenar_por == "Concluídas primeiro":
        tarefas_filtradas.sort(key=lambda x: x["concluida"], reverse=True)
    elif ordenar_por == "Pendentes primeiro":
        tarefas_filtradas.sort(key=lambda x: x["concluida"])

    # Exibir tarefas
    st.markdown("---")

    for tarefa in tarefas_filtradas:
        col1, col2 = st.columns([0.1, 0.9])
        
        with col1:
            # Checkbox para marcar como concluída
            status_atual = tarefa["concluida"]
            novo_status = st.checkbox(
                f"Concluir tarefa: {tarefa['nome']}",
                value=status_atual,
                key=f"checkbox_{tarefa['id']}",
                help="Marque para concluir a tarefa",
                label_visibility="collapsed",
            )
            
            # Atualizar status se houve mudança
            if novo_status != status_atual:
                atualizar_status_tarefa(tarefa["id"], novo_status)
                st.rerun()

        with col2:
            # Exibir nome da tarefa com formatação baseada no status
            if tarefa["concluida"]:
                st.markdown(f"~~{tarefa['nome']}~~ ✅")
            else:
                st.markdown(f"**{tarefa['nome']}** ⏳")

        st.markdown("---")


def renderizar_acoes_extras() -> None:
    """Exibe controles para remover tarefas concluídas ou limpar toda a lista."""
    if st.session_state.tarefas:
        st.subheader("⚙️ Ações")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🧹 Limpar Concluídas", help="Remove todas as tarefas marcadas como concluídas"):
                tarefas_concluidas = sum(
                    1 for t in st.session_state.tarefas if t["concluida"]
                )
                st.session_state.tarefas = [
                    t for t in st.session_state.tarefas if not t["concluida"]
                ]
                if tarefas_concluidas > 0:
                    st.success(f"✅ {tarefas_concluidas} tarefa(s) concluída(s) removida(s)!")
                    st.rerun()
                else:
                    st.info("ℹ️ Não há tarefas concluídas para remover.")

        with col2:
            if st.button("🗑️ Limpar Todas", help="Remove todas as tarefas da lista"):
                total_tarefas = len(st.session_state.tarefas)
                if total_tarefas > 0:
                    st.session_state.tarefas = []
                    st.success(f"✅ {total_tarefas} tarefa(s) removida(s)!")
                    st.rerun()
                else:
                    st.info("ℹ️ Não há tarefas para remover.")


def main() -> None:
    """
    Configura a página, inicializa o estado e renderiza a interface.

    Execute a aplicação com `python -m streamlit run app.py`.
    """
    # Configuração da página
    st.set_page_config(
        page_title="Gerenciador de Tarefas",
        page_icon="📋",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Inicializar estado da sessão
    inicializar_session_state()
    
    # Renderizar componentes da interface
    renderizar_cabecalho()
    renderizar_formulario_adicionar()
    st.markdown("---")
    renderizar_lista_tarefas()
    st.markdown("---")
    renderizar_acoes_extras()
    
    # Rodapé
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Desenvolvido com ❤️ usando Python e Streamlit"
        "</div>",
        unsafe_allow_html=True
    )


# Executar a aplicação
if __name__ == "__main__":
    main()
