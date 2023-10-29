class Deque:
    """Essa é uma classe que simboliza um deque, ou seja, uma estrutura de dados que recebe elementos tanto no início,
    quanto no final. A mesma descrição se aplica também à remoção de itens."""

    def __init__(self):
        self.deque = []

    def insere(self, item):
        """Insere um item no início da lista."""
        self.deque.insert(0, item)

    def insere_final(self, item):
        """Insere um item no final da lista."""
        self.deque.append(item)

    def remove(self):
        """Se houver elementos no deque, remove o primeiro elemento."""
        if self.deque:
            self.deque.pop(0)

    def remove_final(self):
        """Se houver elementos no deque, remove o último elemento."""
        if self.deque:
            self.deque.pop()
