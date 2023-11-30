# Incompleta
# Questão 2 - Busca e Ordenação
def confere_peso(objeto, key):
    i = 0
    comparado = ""
    for j, elem in enumerate(objeto):
        if j == 0:
            comparado == elem[key]
        elif comparado == elem[key]:
            i += 1
        else:
            break

    return i


def confere_altura(objeto, key):
    i = 0
    comparado = ""
    for j, elem in enumerate(objeto):
        if j == 0:
            comparado == elem[key]
        elif comparado == elem[key]:
            i += 1

    return i


qtd_pretendentes = int(input())
pretendentes = []

# Faz a coleta dos dados dos pretendentes
for _ in range(qtd_pretendentes):
    nome, sobrenome, altura, peso = input().split()
    altura = abs(int(altura) - 180)
    peso = int(peso) - 75
    pretendente = [nome, sobrenome, altura, peso]
    pretendentes.append(pretendente)

# Ordena os rapazes pela altura
pretendentes = sorted(pretendentes, key=lambda x: x[2])

# Confere se há pretendentes da mesma altura
msm_altura = confere_altura(pretendentes, 2)

# Ordena os rapazes baseado no peso
if msm_altura != 0:
    lista_aux = pretendentes[:msm_altura+1]
    lista_aux = sorted(lista_aux, key=lambda x: x[3])

    for i in range(msm_altura):
        pretendentes[i] = lista_aux[i]

# Confere se há pretendentes com o msm peso
msm_peso = confere_peso(pretendentes, 3)

# Ordena baseado no primeiro nome
if msm_peso != 0:
    lista_aux = pretendentes[:msm_peso+1]
    lista_aux = sorted(lista_aux, key=lambda x: x[0])

    for i in range(msm_altura):
        pretendentes[i] = lista_aux[i]

print(pretendentes)
