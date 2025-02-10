from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Mock database (armazenará os usuários temporariamente)
users = []

@app.route('/users', methods=['GET'])
def get_users():
    """Retorna todos os usuários cadastrados."""
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    """Recebe os dados do usuário via JSON e os armazena no mock database."""
    try:
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return jsonify({"error": "Campos obrigatórios ausentes"}), 400

        # Salvar usuário no mock database
        users.append({"email": data["email"], "password": data["password"]})
        return jsonify({"message": "Usuário criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": f"Erro no servidor: {str(e)}"}), 500

@app.route('/users/clear', methods=['DELETE'])
def clear_users():
    """Remove todos os usuários cadastrados (opcional para testes)."""
    global users
    users = []
    return jsonify({"message": "Todos os usuários foram removidos"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)