class Nodo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, idade):
        novo = Nodo(nome, idade)
        if self.raiz is None:
            self.raiz = novo
        else:
            self._inserir_recursivo(self.raiz, novo)

    def _inserir_recursivo(self, atual, novo):
        if novo.idade < atual.idade:
            if atual.esquerda is None: atual.esquerda = novo
            else: self._inserir_recursivo(atual.esquerda, novo)
        else:
            if atual.direita is None: atual.direita = novo
            else: self._inserir_recursivo(atual.direita, novo)

    def em_ordem(self, nodo):
        if nodo:
            self.em_ordem(nodo.esquerda)
            print(f"{nodo.nome} ({nodo.idade} anos)")
            self.em_ordem(nodo.direita)

# Exemplo de Uso
bst = ArvoreBinariaDeBusca()
bst.inserir("Camila", 25)
bst.inserir("Gabriel", 28)
bst.inserir("Maria", 20)
print("Lista de Pessoas (Crescente por Idade):")
bst.em_ordem(bst.raiz)