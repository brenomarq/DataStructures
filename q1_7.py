# Introdução - Questão 7
def eh_primo(n: int):
    qtd_divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd_divisores += 1

    if qtd_divisores > 2:
        return False
    return True


def primos_gemeos(n):
    primosgemeos = []

    i = 3
    while len(primosgemeos) < n:
        gemeos = []

        if eh_primo(i):
            gemeos.append(i)
            if eh_primo(i+2):
                gemeos.append(i+2)
                i += 2
                primosgemeos.append(tuple(gemeos))
            else:
                i += 1
        else:
            i += 1

    return primosgemeos
