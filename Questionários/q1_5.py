# Introdução - Questão 5
while True:
    try:
        qtd_buracos = int(input())
        coordenadas_buracos = list()
        
        coordenadas_coelho = tuple(map(float, input().split()))
        coordenadas_raposa = tuple(map(float, input().split()))

        for _ in range(qtd_buracos):
            coordenadas_buraco = tuple(map(float, input().split()))
            coordenadas_buracos.append(coordenadas_buraco)

        for buraco in coordenadas_buracos:
            distancia_coelho = ((coordenadas_coelho[0] - buraco[0])**2 + (coordenadas_coelho[1] - buraco[1])**2)**(0.5)
            distancia_raposa = ((coordenadas_raposa[0] - buraco[0])**2 + (coordenadas_raposa[1] - buraco[1])**2)**(0.5)

            if distancia_coelho <= (distancia_raposa/2):
                print(f"O coelho pode escapar pelo buraco ({buraco[0]:.3f}, {buraco[1]:.3f}).")
                break
        else:
            print("O coelho nao pode escapar.")

    except EOFError:
        break
