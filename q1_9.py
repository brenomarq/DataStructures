# Introdução - Questão 9
num_testes = int(input())

for i in range(num_testes):
    string = input()
    letras = []
    vezes = []

    i = 0
    while i < len(string):
        if not string[i].isnumeric():
            letras.append(string[i])
            i += 1
        else:
            num = ''
            while i < len(string) and string[i].isnumeric():
                num += string[i]
                i += 1
            vezes.append(int(num))

    nova_string = ''
    for i in range(len(letras)):
        nova_string += letras[i] * vezes[i]

    print(nova_string)
