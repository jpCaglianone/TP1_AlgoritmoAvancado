class HeapMinimo:
    def __init__(self):
        self.heap = []

    def pai(self, i):
        return (i - 1) // 2

    def filho_esquerdo(self, i):
        return 2 * i + 1

    def filho_direito(self, i):
        return 2 * i + 2

    def trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):
        pai = self.pai(i)
        if i > 0 and self.heap[i] < self.heap[pai]:
            self.trocar(i, pai)
            self._subir(pai)

    def _descer(self, i):
        indice_menor = i
        esquerdo = self.filho_esquerdo(i)
        direito = self.filho_direito(i)

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[indice_menor]:
            indice_menor = esquerdo

        if direito < len(self.heap) and self.heap[direito] < self.heap[indice_menor]:
            indice_menor = direito

        if indice_menor != i:
            self.trocar(i, indice_menor)
            self._descer(indice_menor)

    def obter_minimo(self):
        if not self.heap:
            return None
        return self.heap[0]

    def remover(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        valor_minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)

        return valor_minimo

if __name__ == "__main__":
    heap = HeapMinimo()

    valores = [10, 5, 15, 3, 8, 1, 20]
    print("\nInserindo valores:", valores)
    for valor in valores:
        heap.inserir(valor)
        print(f"Após inserir {valor}: {heap.heap}")

    print("\nRemovendo valores:")
    while heap.heap:
        removido = heap.remover()
        print(f"Valor removido: {removido}, Heap atual: {heap.heap}")