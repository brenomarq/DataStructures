# Introdução - Questão 3
qtd_lesmas = int(input())
velocidades = list()

for i in range(qtd_lesmas):
    velocidade = int(input())
    velocidades.append(velocidade)

categorias = {
    "a": [0],
    "b": [0],
    "c": [0]
}

for v in velocidades:
    if v < 10:
        categorias["a"].append(v)
    elif 10 <= v < 20:
        categorias["b"].append(v)
    else:
        categorias["c"].append(v)

print(f"{max(categorias['a'])} {max(categorias['b'])} {max(categorias['c'])}")
