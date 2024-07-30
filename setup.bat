@echo off
setlocal

REM Diretório de destino para downloads
set DOWNLOAD_DIR=%~dp0downloads
mkdir "%DOWNLOAD_DIR%"

REM URLs dos instaladores
set PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
set GIT_INSTALLER_URL=https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe
set DOCKER_INSTALLER_URL=https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe

REM Caminhos dos instaladores baixados
set PYTHON_INSTALLER=%DOWNLOAD_DIR%\python-3.11.0-amd64.exe
set GIT_INSTALLER=%DOWNLOAD_DIR%\Git-2.31.1-64-bit.exe
set DOCKER_INSTALLER=%DOWNLOAD_DIR%\DockerDesktopInstaller.exe

REM Verificar e baixar Python
if not exist "%PYTHON_INSTALLER%" (
    echo Baixando Python...
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER_URL% -OutFile %PYTHON_INSTALLER%"
)

REM Verificar e baixar Git
if not exist "%GIT_INSTALLER%" (
    echo Baixando Git...
    powershell -Command "Invoke-WebRequest -Uri %GIT_INSTALLER_URL% -OutFile %GIT_INSTALLER%"
)

REM Verificar e baixar Docker
if not exist "%DOCKER_INSTALLER%" (
    echo Baixando Docker...
    powershell -Command "Invoke-WebRequest -Uri %DOCKER_INSTALLER_URL% -OutFile %DOCKER_INSTALLER%"
)

REM Instalar Python
where python || (
    echo Instalando Python...
    "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1
    set PATH=%PATH%;C:\Program Files\Python311;C:\Program Files\Python311\Scripts
)

REM Instalar dependências Python
echo Instalando dependências do Python...
pip install -r requirements.txt

REM Instalar Git
where git || (
    echo Instalando Git...
    "%GIT_INSTALLER%" /silent
)

REM Instalar Docker
where docker || (
    echo Instalando Docker...
    "%DOCKER_INSTALLER%" install --quiet
)

REM Construir e iniciar containers Docker
echo Construindo e iniciando containers Docker...
docker-compose build
docker-compose up -d

echo Setup completo! Inicie o software principal.

endlocal
