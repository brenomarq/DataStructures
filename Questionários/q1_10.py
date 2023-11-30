# Introdução - Questão 10
qtd_jogadores = int(input())

habilidades = [int(x) for x in input().split()]
habilidades.sort(reverse=True)

t = 0  # Habilidade dos titulares
r = 0  # Habilidade do reserva
for i in range(len(habilidades)):
    if i <= 10:
        t += habilidades[i]
    elif i >= 11 and i <= 21:
        r += habilidades[i]

print(t-r)  # Diferença entre as habilidades
