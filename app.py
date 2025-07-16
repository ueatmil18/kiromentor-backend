from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a KiroMentor Backend"

@app.route('/explicar', methods=['POST'])
def explicar_codigo():
    data = request.json
    codigo = data.get('codigo', '')
    explicacion = f"Este código parece un bucle o estructura común: {codigo[:30]}..."
    return jsonify({"codigo": codigo, "explicacion": explicacion})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
