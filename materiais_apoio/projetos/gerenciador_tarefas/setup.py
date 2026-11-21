"""
Script de Setup para o Gerenciador de Tarefas

Este script automatiza a instalação das dependências e execução da aplicação.
"""

import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent


def verificar_python() -> bool:
    """Verifica se o interpretador atual atende ao requisito Python 3.8+."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("ERRO: Python 3.8+ e necessario")
        print(f"Versão atual: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"OK: Python {version.major}.{version.minor}.{version.micro} detectado")
    return True


def instalar_dependencias() -> bool:
    """Instala as dependências declaradas no requirements.txt do projeto."""
    print("Instalando dependencias...")
    
    try:
        requirements_path = PROJECT_DIR / "requirements.txt"
        if requirements_path.exists():
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    str(requirements_path),
                ]
            )
        else:
            # Instalar streamlit diretamente
            subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit>=1.28.0"])
        
        print("OK: Dependencias instaladas com sucesso!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"ERRO: Falha ao instalar dependencias: {e}")
        return False


def verificar_streamlit() -> bool:
    """Confirma que o Streamlit pode ser importado pelo Python atual."""
    try:
        import streamlit
        print(f"OK: Streamlit {streamlit.__version__} instalado")
        return True
    except ImportError:
        print("ERRO: Streamlit nao encontrado")
        return False


def executar_aplicacao() -> bool:
    """Inicia o app.py localizado nesta pasta usando o interpretador atual."""
    app_path = PROJECT_DIR / "app.py"
    
    if not app_path.exists():
        print("ERRO: Arquivo app.py nao encontrado!")
        return False
    
    print("Iniciando aplicacao...")
    print("A aplicacao sera aberta em: http://localhost:8501")
    print("Para parar a aplicacao, pressione Ctrl+C")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", str(app_path)],
            cwd=str(PROJECT_DIR),
            check=True,
        )
        return True
    except KeyboardInterrupt:
        print("\nAplicacao finalizada pelo usuario")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERRO: Falha ao executar aplicacao: {e}")
        return False


def main() -> int:
    """Valida o ambiente, instala dependências e opcionalmente inicia o app."""
    print("=" * 50)
    print("GERENCIADOR DE TAREFAS - SETUP")
    print("=" * 50)
    
    # Verificar Python
    if not verificar_python():
        return 1
    
    # Instalar dependências
    if not instalar_dependencias():
        print("ERRO: Falha na instalacao das dependencias")
        return 1
    
    # Verificar instalação do Streamlit
    if not verificar_streamlit():
        print("ERRO: Falha na verificacao do Streamlit")
        return 1
    
    print("\n" + "=" * 50)
    print("SETUP CONCLUIDO COM SUCESSO!")
    print("=" * 50)
    
    # Perguntar se deseja executar a aplicação
    resposta = input("\nDeseja executar a aplicacao agora? (s/n): ").lower().strip()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        print()
        return 0 if executar_aplicacao() else 1
    else:
        print("\nPara executar manualmente, use: streamlit run app.py")
        print("URL da aplicacao: http://localhost:8501")
        return 0


if __name__ == "__main__":
    sys.exit(main())
