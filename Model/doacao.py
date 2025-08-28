from datetime import datetime


class Doacaa:
    pass

class Item:
    pass

class Usuario:
    pass


class Doacao:
    def  __init__(self, tipo, descricao, quantidade, doador, data=None):
        self.tipo = tipo
        self.descricao = descricao
        self.quantidade = quantidade
        self.doador = doador
        self.data = data if data else datetime.now().strftime("%d%m%Y %H:%M")
    
    def __str__(self):
        return{
            "tipo": self.tipo,
            "descricao": self.descricao,
            "quantidade": self.quantidade,
            "doador": self.doador,
            "data":self.data
            
        }
    