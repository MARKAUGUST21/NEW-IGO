from flask import Blueprint, render_template, request, redirect, url_for
from Model.doacao import Usuario, Item, Doacao

doacao_bp = Blueprint('doacao', __name__)

doacoes = []

@doacao_bp.route('/doacoes', methods=['GET', 'POST'])
def doacoes_view():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        quantidade = request.form.get('quantidade')
        tamanho = request.form.get('tamanho')
        usuario_nome = request.form.get('usuario')

        usuario = Usuario(1, usuario_nome, '', '')
        item = Item(tipo, quantidade, tamanho)
        doacao = Doacao(usuario, [item])
        doacoes.append(doacao)
        return redirect(url_for('doacao.doacoes_view'))

    return render_template('doacoes.html', doacoes=doacoes)
