# Deque e lista - Questão 3
def exibe_candidatos(deque, pos, ordem):
    if ordem == "direta":
        for _ in range(pos):
            deque.remove_front()
        while deque.size() != 0:
            print(deque.remove_front())
    elif ordem == "inversa":
        qtd = deque.size()-1 - pos
        for _ in range(qtd):
            deque.remove_rear()
        while deque.size() != 0:
            print(deque.remove_rear())
