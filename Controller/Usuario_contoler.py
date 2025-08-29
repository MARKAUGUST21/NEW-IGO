from Models.usario import Usuario

usuarios = [] # por enquanto guardar memoria 

def cadastrar_usuario(nome, email):
    nome_usuario = Usuario(nome, email)
    usarios.append(novo_usuario)    
    return nome_usuario

def listar_usuario():
    return usuarios