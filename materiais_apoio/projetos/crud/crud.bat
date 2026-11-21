@echo off
cd /d "%~dp0"
echo ========================================
echo     CRUD PESSOA
echo ========================================
echo.

:: Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado! Instale Python 3.8 ou superior.
    pause
    exit /b 1
)

echo OK: Python detectado

:: Executar aplicação
echo.
echo ========================================
echo         INICIANDO APLICACAO
echo ========================================
echo.
echo 🚀 A aplicacao sera aberta em: http://localhost:8501
echo 💡 Para parar a aplicacao, pressione Ctrl+C
echo.

python app.py

pause
