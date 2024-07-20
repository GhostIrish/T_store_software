FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

EXPOSE 5000

CMD ["python", "app.py"]
