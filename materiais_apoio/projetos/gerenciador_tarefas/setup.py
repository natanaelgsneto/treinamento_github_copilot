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
        print("❌ Erro: Python 3.8+ é necessário")
        print(f"Versão atual: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True


def instalar_dependencias() -> bool:
    """Instala as dependências declaradas no requirements.txt do projeto."""
    print("🔧 Instalando dependências...")
    
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
        
        print("✅ Dependências instaladas com sucesso!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False


def verificar_streamlit() -> bool:
    """Confirma que o Streamlit pode ser importado pelo Python atual."""
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} instalado")
        return True
    except ImportError:
        print("❌ Streamlit não encontrado")
        return False


def executar_aplicacao() -> bool:
    """Inicia o app.py localizado nesta pasta usando o interpretador atual."""
    app_path = PROJECT_DIR / "app.py"
    
    if not app_path.exists():
        print("❌ Arquivo app.py não encontrado!")
        return False
    
    print("🚀 Iniciando aplicação...")
    print("📌 A aplicação será aberta em: http://localhost:8501")
    print("💡 Para parar a aplicação, pressione Ctrl+C")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", str(app_path)],
            cwd=str(PROJECT_DIR),
            check=True,
        )
        return True
    except KeyboardInterrupt:
        print("\n👋 Aplicação finalizada pelo usuário")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar aplicação: {e}")
        return False


def main() -> int:
    """Valida o ambiente, instala dependências e opcionalmente inicia o app."""
    print("=" * 50)
    print("📋 GERENCIADOR DE TAREFAS - SETUP")
    print("=" * 50)
    
    # Verificar Python
    if not verificar_python():
        return 1
    
    # Instalar dependências
    if not instalar_dependencias():
        print("❌ Falha na instalação das dependências")
        return 1
    
    # Verificar instalação do Streamlit
    if not verificar_streamlit():
        print("❌ Falha na verificação do Streamlit")
        return 1
    
    print("\n" + "=" * 50)
    print("✅ SETUP CONCLUÍDO COM SUCESSO!")
    print("=" * 50)
    
    # Perguntar se deseja executar a aplicação
    resposta = input("\n🚀 Deseja executar a aplicação agora? (s/n): ").lower().strip()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        print()
        return 0 if executar_aplicacao() else 1
    else:
        print("\n💡 Para executar manualmente, use: streamlit run app.py")
        print("📌 URL da aplicação: http://localhost:8501")
        return 0


if __name__ == "__main__":
    sys.exit(main())
