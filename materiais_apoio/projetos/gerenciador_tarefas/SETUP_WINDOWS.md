# Setup no Windows

## Requisitos

- Python 3.8 ou superior disponível como `python` no PowerShell.
- A dependência de execução é Streamlit (`streamlit>=1.28.0`), declarada em
  `requirements.txt`.

## Instalação recomendada

Abra o PowerShell na raiz do repositório e execute:

```powershell
cd .\materiais_apoio\projetos\gerenciador_tarefas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Se a ativação do ambiente virtual for bloqueada pela política do PowerShell,
execute `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
uma vez, ou use o terminal do VS Code configurado para executar o script.

## Iniciar o aplicativo

Com o ambiente virtual ativo e o terminal na pasta do projeto:

```powershell
python -m streamlit run app.py
```

Abra http://localhost:8501 no navegador. Para encerrar, pressione `Ctrl+C` no
terminal.

## Opções automatizadas

- `python setup.py`: instala as dependências usando o Python atual e pergunta se
  deve iniciar o aplicativo. Ative o ambiente virtual antes para não instalar
  pacotes globalmente.
- `.\executar.bat`: instala as dependências e inicia o aplicativo com o Python
  encontrado no PATH. Também é recomendado ativar o ambiente virtual antes de
  usá-lo.

Para executar os testes, instale pytest separadamente e rode o comando de teste:

```powershell
python -m pip install pytest
python -m pytest -q
```

Pytest não é necessário para executar o aplicativo.
