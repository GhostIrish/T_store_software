# Use a imagem base do Python
FROM python:3.11-slim

LABEL org.opencontainers.image.authors="harielpimenta@hotmail.com"

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    tk \
    libx11-dev \
    libxft-dev \
    libxext-dev \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do aplicativo para o contêiner
COPY . .

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=main.py

# Expor a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
