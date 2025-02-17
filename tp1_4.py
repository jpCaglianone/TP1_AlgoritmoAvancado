class HeapMinimo:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):
        pai = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[pai]:
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            self._subir(pai)

    def remover(self):
        if not self.heap:
            return None

        valor_minimo = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return valor_minimo

        self.heap[0] = self.heap.pop()
        self._reorganizar_descendo(0)

        return valor_minimo

    def _reorganizar_descendo(self, i):
        menor = i
        esquerdo = 2 * i + 1
        direito = 2 * i + 2

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo

        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._reorganizar_descendo(menor)


if __name__ == "__main__":
    heap = HeapMinimo()
    valores = [10, 5, 15, 3, 8, 1, 20]
    print("\nTestando segunda implementação:")
    print("Inserindo valores:", valores)

    for valor in valores:
        heap.inserir(valor)
        print(f"Após inserir {valor}: {heap.heap}")

    print("\nRemovendo valores (sempre remove o menor):")
    while heap.heap:
        removido = heap.remover()
        print(f"Valor removido: {removido}, Heap atual: {heap.heap}")