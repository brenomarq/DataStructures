# Incompleta
# Questão 2 - Busca e Ordenação
def confere_igualdade(lista ,key):
    i = 0
    comparado = 0
    for l, elem in enumerate(lista):
        if l == 0:
            comparado = elem[key]
        elif elem[key] == comparado:
            i += 1
    
    if i > 0:
        return False
    return True

qtd_homens = int(input())
homens = []

for i in range(qtd_homens):
    nome, sobrenome, altura, peso = input().split()
    altura = abs(int(altura) - 180)
    peso = int(peso)
    homem = [nome, sobrenome, altura, peso]
    homens.append(homem)

homens = sorted(homens, key=lambda x: x[2], reverse=True)

if confere_igualdade(homens, 3):
    print(f"Qualquer coisa")
