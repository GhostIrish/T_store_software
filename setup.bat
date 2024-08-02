@echo off
setlocal

REM Caminho para o arquivo requirements.txt
set REQUIREMENTS_FILE=%~dp0requirements.txt

REM Construir e iniciar containers Docker
echo Construindo e iniciando containers Docker...
docker-compose build
docker-compose up -d

REM Verificar se o arquivo requirements.txt existe
if exist "%REQUIREMENTS_FILE%" (
    echo Instalando dependências do Python...
    pip install -r "%REQUIREMENTS_FILE%"
) else (
    echo "requirements.txt não encontrado. Certifique-se de que o arquivo está no mesmo diretório que este script."
)

REM Executar o script para criar o banco de dados
echo Executando script de criação do banco de dados...
pushd backend
python database_create.py
popd

echo Setup completo! Inicie a API e em seguida o software principal.

endlocal
