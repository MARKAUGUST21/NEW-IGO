from flask import Flask, render_template, request, jsonify
from Controller.Usuario_contoler import cadastrar_usuario, listar_usuario

app = Flask(__name__)

@app.route('/')
def index():
    # Rederiza o HTML de login
    return render_template('login.html')
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    
    if not nome or not email:
        return jsonify ({"status,": "sucesso", "nome": usuario.nome, "email": usario.email})
@app.route('/usuarios', methods=['GET'])
def usuarios():
    lista = [{"nome": u.nome, "email": u.email} for u in listar_usuario()]
    return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True)