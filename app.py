from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde otros orígenes (como GitHub Pages)

@app.route('/')
def index():
    return "Bienvenido a KiroMentor Backend. Usá POST en /explicar."

@app.route('/explicar', methods=['POST'])
def explicar_codigo():
    data = request.get_json()
    
    if not data or 'codigo' not in data:
        return jsonify({"error": "Falta el campo 'codigo' en el cuerpo JSON"}), 400

    codigo = data['codigo']
    
    # Simulación de explicación básica
    explicacion = f"Este código parece un bucle o estructura común: {codigo[:50]}..."

    return jsonify({
        "codigo": codigo,
        "explicacion": explicacion
    })

# Opción útil para pruebas desde navegador (evita error 405 si accedés por GET)
@app.route('/explicar', methods=['GET'])
def explicar_get():
    return "Este endpoint acepta solo POST con JSON para explicar código."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
