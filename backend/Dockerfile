# Use a imagem base do Python
FROM python:3.11-slim

LABEL org.opencontainers.image.authors="harielpimenta@hotmail.com"

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do aplicativo para o contêiner
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=main.py

# Expõe a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
