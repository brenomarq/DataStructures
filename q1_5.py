# Introdução - Questão 5
# Precisa de atualização...
while True:
    try:
        qtd_buracos = int(input())
        x_buracos = list()
        y_buracos = list()

        x_coelho, y_coelho = map(float, input().split())
        x_raposa, y_raposa = map(float, input().split())

        for i in range(qtd_buracos):
            x_buraco, y_buraco = map(float, input().split())
            x_buracos.append(x_buraco)
            y_buracos.append(y_buraco)

        buracos_possiveis = list()
        for i in range(qtd_buracos):
            distancia_coelho = ((x_coelho-x_buracos[i])**2 * (y_coelho-y_buracos[i])**2)*1/2
            distancia_raposa = ((x_raposa-x_buracos[i])**2 * (y_raposa-y_buracos[i])**2)*1/2

            if distancia_coelho <= distancia_raposa/2:
                buracos_possiveis.append((x_buracos[i], y_buracos[i]))

        if buracos_possiveis:
            print(f"O coelho pode escapar pelo buraco ({buracos_possiveis[0][0]:.3f}, {buracos_possiveis[0][1]:.3f}).")
        else:
            print("O coelho nao pode escapar.")


    except EOFError:
        break
