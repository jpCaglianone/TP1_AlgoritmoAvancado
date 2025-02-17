class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False


class TrieAutocomplete:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no = self.raiz
        for letra in palavra:
            if letra not in no.filhos:
                no.filhos[letra] = NoTrie()
            no = no.filhos[letra]
        no.fim_palavra = True

    def _encontrar_no(self, prefixo):
        no = self.raiz
        for letra in prefixo:
            if letra not in no.filhos:
                return None
            no = no.filhos[letra]
        return no

    def _coletar_palavras(self, no, prefixo, palavras):
        if no.fim_palavra:
            palavras.append(prefixo)

        for letra, filho in no.filhos.items():
            self._coletar_palavras(filho, prefixo + letra, palavras)

    def buscar_por_prefixo(self, prefixo):
        no = self._encontrar_no(prefixo)
        if not no:
            return []

        palavras = []
        self._coletar_palavras(no, prefixo, palavras)
        return palavras


if __name__ == "__main__":
    trie = TrieAutocomplete()

    palavras = [
        "python", "programacao", "programa", "programador",
        "projeto", "desenvolvimento", "dados", "database",
        "desenvolvedor", "debug", "debugar"
    ]

    print("\nInserindo palavras no sistema:")
    for palavra in palavras:
        trie.inserir(palavra)
        print(f"Inserida: {palavra}")

    prefixos_teste = ["pro", "des", "da", "de", "prog"]

    print("\nTestando autocomplete:")
    for prefixo in prefixos_teste:
        sugestoes = trie.buscar_por_prefixo(prefixo)
        print(f"\nPrefixo '{prefixo}':")
        for sugestao in sugestoes:
            print(f"  - {sugestao}")