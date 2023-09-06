# Introdução - Questão 1
def divisores(n: int):
    div = list()

    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)

    return div
