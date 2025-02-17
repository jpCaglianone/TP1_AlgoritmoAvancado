class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False


class VerificadorOrtografico:
    def __init__(self):
        self.dicionario = NoTrie()
        self.distancia_maxima = 1

    def inserir_palavra(self, palavra):
        no = self.dicionario
        for letra in palavra.lower():
            if letra not in no.filhos:
                no.filhos[letra] = NoTrie()
            no = no.filhos[letra]
        no.fim_palavra = True

    def _calcular_distancia(self, palavra1, palavra2):
        if len(palavra1) < len(palavra2):
            return self._calcular_distancia(palavra2, palavra1)

        if len(palavra2) == 0:
            return len(palavra1)

        linha_anterior = range(len(palavra2) + 1)

        for i, c1 in enumerate(palavra1):
            linha_atual = [i + 1]
            for j, c2 in enumerate(palavra2):
                insercoes = linha_anterior[j + 1] + 1
                delecoes = linha_atual[j] + 1
                substituicoes = linha_anterior[j] + (c1 != c2)
                linha_atual.append(min(insercoes, delecoes, substituicoes))
            linha_anterior = linha_atual

        return linha_anterior[-1]

    def _coletar_palavras(self, no, palavra_atual, palavras):
        if no.fim_palavra:
            palavras.append(palavra_atual)
        for letra, filho in no.filhos.items():
            self._coletar_palavras(filho, palavra_atual + letra, palavras)

    def sugerir_correcoes(self, palavra):
        todas_palavras = []
        self._coletar_palavras(self.dicionario, "", todas_palavras)

        sugestoes = []
        for palavra_dict in todas_palavras:
            distancia = self._calcular_distancia(palavra.lower(), palavra_dict)
            if distancia <= self.distancia_maxima:
                sugestoes.append((palavra_dict, distancia))

        return sorted(sugestoes, key=lambda x: x[1])


if __name__ == "__main__":
    verificador = VerificadorOrtografico()

    dicionario = [
        "casa", "carro", "computador", "mouse",
        "teclado", "monitor", "programa", "python",
        "desenvolvimento", "programador"
    ]

    print("\nCarregando dicionário:")
    for palavra in dicionario:
        verificador.inserir_palavra(palavra)
        print(f"Inserida: {palavra}")

    palavras_teste = ["caza", "progama", "dezenvolvimento", "mause", "tecladu"]

    print("\nTestando corretor ortográfico:")
    for palavra in palavras_teste:
        print(f"\nPalavra: {palavra}")
        sugestoes = verificador.sugerir_correcoes(palavra)
        if sugestoes:
            print("Sugestões:")
            for sugestao, distancia in sugestoes:
                print(f"  - {sugestao} (distância: {distancia})")
        else:
            print("Nenhuma sugestão encontrada")