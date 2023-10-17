# Introdução - Questão 8
qtd_linhas = int(input())
linhas = list()

for _ in range(qtd_linhas):
	linha = input()
	linhas.append(linha)

for linha in linhas:
    qtd_1 = linha.count("1")
    conta_1 = 0
    conta_0 = 0

    if qtd_1 == 0:
         print(conta_0)
         continue

    i = 0
    while linha[i] != "1":
        i += 1
    while conta_1 != qtd_1 and i < len(linha):
        if linha[i] == "1":
            conta_1 += 1
        else:
            conta_0 += 1
        i += 1

    print(conta_0)
