#!/bin/bash

@echo off
REM Instalar Docker (se não estiver instalado)
if not exist "%ProgramFiles%\Docker\Docker" (
    echo Docker is not installed. Installing Docker...
    powershell -Command "Start-Process 'https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe' -Wait -NoNewWindow"
)

REM Iniciar Docker
echo Starting Docker...
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
timeout /t 30

REM Navegar para a pasta do projeto
cd %~dp0

REM Configurar banco de dados e API usando docker-compose
echo Setting up MySQL container and API...
docker-compose up -d

REM Esperar alguns segundos para garantir que o container está completamente iniciado
timeout /t 15

REM Iniciar a aplicação GUI
echo Starting the GUI application...
start "" "%~dp0dist\main.exe"

echo Setup complete.
pause
