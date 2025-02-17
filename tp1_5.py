class CalculadorHeap:
    def indice_pai(self, i):
        return (i - 1) // 2

    def indice_filho_esquerdo(self, i):
        return 2 * i + 1

    def indice_filho_direito(self, i):
        return 2 * i + 2

    def imprimir_indices(self, indice):
        print(f"\nPara o nó no índice {indice}:")
        print(f"Pai: {self.indice_pai(indice)}")
        print(f"Filho Esquerdo: {self.indice_filho_esquerdo(indice)}")
        print(f"Filho Direito: {self.indice_filho_direito(indice)}")


if __name__ == "__main__":
    calc = CalculadorHeap()

    for i in range(5):
        calc.imprimir_indices(i)