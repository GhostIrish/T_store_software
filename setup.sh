#!/bin/bash

echo "Instalando Docker..."
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

echo "Configurando o ambiente..."
docker-compose up -d

echo "Instalação completa. O aplicativo está rodando em http://localhost:5000"
