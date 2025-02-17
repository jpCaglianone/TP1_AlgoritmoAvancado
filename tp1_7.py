class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

    def __lt__(self, other):
        return self.prioridade < other.prioridade


class FilaPrioridade:
    def __init__(self):
        self.tarefas = []

    def inserir_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        self._subir(len(self.tarefas) - 1)

    def obter_proxima_tarefa(self):
        if not self.tarefas:
            return None

        if len(self.tarefas) == 1:
            return self.tarefas.pop()

        tarefa = self.tarefas[0]
        self.tarefas[0] = self.tarefas.pop()
        self._descer(0)
        return tarefa

    def _subir(self, i):
        pai = (i - 1) // 2
        if i > 0 and self.tarefas[i].prioridade < self.tarefas[pai].prioridade:
            self.tarefas[i], self.tarefas[pai] = self.tarefas[pai], self.tarefas[i]
            self._subir(pai)

    def _descer(self, i):
        menor = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < len(self.tarefas) and self.tarefas[esq].prioridade < self.tarefas[menor].prioridade:
            menor = esq

        if dir < len(self.tarefas) and self.tarefas[dir].prioridade < self.tarefas[menor].prioridade:
            menor = dir

        if menor != i:
            self.tarefas[i], self.tarefas[menor] = self.tarefas[menor], self.tarefas[i]
            self._descer(menor)


if __name__ == "__main__":
    fila = FilaPrioridade()

    tarefas = [
        ("Reunião com cliente", 2),
        ("Enviar relatório", 1),
        ("Atualizar sistema", 3),
        ("Responder emails", 1),
        ("Backup de dados", 2)
    ]

    print("\nInserindo tarefas:")
    for desc, prio in tarefas:
        tarefa = Tarefa(desc, prio)
        fila.inserir_tarefa(tarefa)
        print(f"Tarefa: {desc} (Prioridade: {prio})")

    print("\nProcessando tarefas por prioridade:")
    while True:
        tarefa = fila.obter_proxima_tarefa()
        if not tarefa:
            break
        print(f"Executando: {tarefa.descricao} (Prioridade: {tarefa.prioridade})")