#!/bin/bash

echo "=============================="
echo " Iniciando Setup do Projeto"
echo "=============================="

# Diretório onde o projeto será clonado
PROJECT_DIR="/home/$(whoami)/project_t_store"

# URL do repositório Git
REPO_URL="https://github.com/GhostIrish/T_store_software.git"

# Clonando o repositório
echo "Clonando o repositório do GitHub..."
git clone "$REPO_URL" "$PROJECT_DIR"

# Navegando para o diretório do projeto
cd "$PROJECT_DIR" || exit

# Iniciando Docker Compose
echo "Iniciando serviços do Docker..."
docker-compose up -d

echo "=============================="
echo "Setup concluído com sucesso!"
echo "=============================="
