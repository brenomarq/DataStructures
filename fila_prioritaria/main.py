import json

class Cliente:
    def __init__(self, nome, idade, prioridade):
        self.__nome = nome
        self.__idade = idade
        self.__prioridade = prioridade

    def __repr__(self) -> str:
        return f"{(self.__nome, self.__idade, self.__prioridade)}"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @property
    def prioridade(self):
        return self.__prioridade


class Fila:
    def __init__(self):
        self.__itens = []

    def __repr__(self):
        return f"{self.__itens}"

    @property
    def itens(self):
        return self.__itens

    def adicionar(self, valor: Cliente):
        self.__itens.append(valor)

    def retirar(self):
        if self.__itens:
            return self.__itens.pop(0)
        return "Fila vazia"


fila_mais_velhos = Fila()
fila_prioritarios = Fila()
fila_normal = Fila()


with open("clientes.json", "+r", encoding="utf-8") as arquivo:
    clientes = json.load(arquivo)

pessoas = []
for cliente in clientes:
    item = Cliente(cliente["nome"], cliente["idade"], cliente["prioritario"])
    pessoas.append(item)

# Adiciona os clientes nas filas
for pessoa in pessoas:
    if pessoa.idade >= 85:
        fila_mais_velhos.adicionar(pessoa)
    elif pessoa.idade >= 65 or pessoa.prioridade:
        fila_prioritarios.adicionar(pessoa)
    else:
        fila_normal.adicionar(pessoa)

print(fila_mais_velhos.retirar())
print(fila_mais_velhos)

