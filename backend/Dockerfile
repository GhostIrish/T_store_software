# Usa a imagem base do Python
FROM python:3.11-slim

LABEL org.opencontainers.image.authors="harielpimenta@hotmail.com"

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia apenas o arquivo principal da API e outras dependências necessárias
COPY app.py .
COPY backend/ ./backend/

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Exponha a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
