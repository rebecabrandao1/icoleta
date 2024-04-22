from flask import Flask, request, jsonify

app = Flask(__name__)

pesos_recebidos = []

@app.route('/receber_peso', methods=['POST'])
def receber_peso():
    dados = request.json
    peso = dados.get('peso')
    print(f"Peso recebido: {peso} kg")
    pesos_recebidos.append(peso)
    return jsonify({"mensagem": "Dados recebidos com sucesso"}), 200

@app.route('/pesos', methods=['GET'])
def listar_pesos():

    return jsonify(pesos_recebidos), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
