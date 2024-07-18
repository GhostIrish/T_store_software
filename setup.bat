@echo off
echo ================================
echo  Iniciando Setup do Projeto
echo ================================

REM Diretório onde o projeto será clonado
SET PROJECT_DIR=C:\project_t_store

REM URL do repositório Git
SET REPO_URL=https://github.com/GhostIrish/T_store_software.git

REM Clonando o repositório
echo Clonando o repositório do GitHub...
git clone %REPO_URL% %PROJECT_DIR%

REM Navegando para o diretório do projeto
cd %PROJECT_DIR%

REM Iniciando Docker Compose
echo Iniciando serviços do Docker...
docker-compose up -d

echo ================================
echo Setup concluído com sucesso!
echo ================================
pause
