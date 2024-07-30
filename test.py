import requests

# Supondo que a API está acessível em http://localhost:5000
response = requests.get("http://localhost:5000/api/genders")
print(response.json())
