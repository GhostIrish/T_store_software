from flask import Flask, make_response, jsonify, request
from bd_temporario_teste import lista_roupas

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/clothes', methods=['GET'])
def get_clothes():
    return make_response(
        jsonify(lista_roupas)
        )

@app.route('/clothes', methods=['POST'])
def add_cloth():
    cloth = request.json
    lista_roupas.append(cloth)
    return make_response(
        jsonify(
            message='Product registered sucessfully',
            item=cloth
            )
        )

app.run()