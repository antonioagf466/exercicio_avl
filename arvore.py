from no import No

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def _obter_altura(self, no):
        """Retorna a altura do nó de forma segura (se None, retorna -1)."""
        if no is None:
            return -1
        return no.altura

    def _atualizar_altura(self, no):
        """Atualiza a altura do nó com base na altura de seus filhos."""
        if no:
            no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))

    def _fator_balanceamento(self, no):
        """Calcula o fator: altura_esquerda - altura_direita."""
        if no is None:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)


    def _rotacao_direita(self, y):
        """Rotação simples à direita (caso Esquerda-Esquerda)."""
        """prestar atencao em ambas as rotacoes que passamos y como parametro e x é o filho em questao(seja para esquerda ou direita) e t2 é FILHO DE x
        seja para esquerda ou direita tambem dependendo do caso, e ai rotacionamos para o lado em questao"""
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self._atualizar_altura(y)
        self._atualizar_altura(x)

        return x  

    def _rotacao_esquerda(self, x):
        """Rotação simples à esquerda (caso Direita-Direita)."""
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self._atualizar_altura(x)
        self._atualizar_altura(y)

        return y  


    def inserir(self, numero):
        self.raiz = self._inserir_recursivo(self.raiz, numero)

    def _inserir_recursivo(self, no_atual, numero):
        if no_atual is None:
            return No(numero)
        
        if numero == no_atual.numero:
            return no_atual  
        elif numero < no_atual.numero:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, numero)
        else:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, numero)

        self._atualizar_altura(no_atual)

        balanceamento = self._fator_balanceamento(no_atual)
        """Prestar atencao que o balanceamento nao eh baseado na raiz ele eh baseado POR NO e soh pode ficar desbalanceado quando inserimos ou removemos
        a arvore nao precisa ser simetrica para estar balanceada, e os unicos nos que podem sair de balanceamento sao os que estao envolvidos na troca
        (adicao ou remocao)"""


        if balanceamento > 1 and numero < no_atual.esquerda.numero:
            return self._rotacao_direita(no_atual)

        if balanceamento < -1 and numero > no_atual.direita.numero:
            return self._rotacao_esquerda(no_atual)

        if balanceamento > 1 and numero > no_atual.esquerda.numero:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if balanceamento < -1 and numero < no_atual.direita.numero:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual


    def buscar(self, numero):
        return self._buscar_recursivo(self.raiz, numero)

    def _buscar_recursivo(self, no_atual, numero):
        if no_atual is None or no_atual.numero == numero:
            return no_atual
        if numero < no_atual.numero:
            return self._buscar_recursivo(no_atual.esquerda, numero)
        return self._buscar_recursivo(no_atual.direita, numero)
    
    def calcular_altura(self):
        """folhas 0, raiz o maior numero da altura"""
        return self._obter_altura(self.raiz)
    
    def contar_nos(self):
        """Contagens abaixo, todos os números na arvore são nós mas apenas números que não tem nenhum filho são folhas, 
        ou seja sempre terao mais nós que folhas"""
        return self._contar_nos_recursivo(self.raiz)

    def _contar_nos_recursivo(self, no_atual):
        if no_atual is None:
            return 0
        return 1 + self._contar_nos_recursivo(no_atual.esquerda) + self._contar_nos_recursivo(no_atual.direita)

    def contar_leaves(self): 
        return self.contar_folhas()

    def contar_folhas(self):
        return self._contar_folhas_recursivo(self.raiz)

    def _contar_folhas_recursivo(self, no_atual):
        if no_atual is None:
            return 0
        if no_atual.esquerda is None and no_atual.direita is None:
            return 1
        return self._contar_folhas_recursivo(no_atual.esquerda) + self._contar_folhas_recursivo(no_atual.direita)

    def _obter_menor_no(self, no):
        """Auxiliar para encontrar o nó com o menor valor (mais à esquerda)."""
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover(self, numero):
        """A remocao funciona procurando o numero acima do numero removido que seja mais proximo, ou seja vai para a direita e depois 
        para e esquerda ao maximo possivel, copia o numero que encontra e depois deleta o numero que foi copiado, caso o numero copiado tenha um filho a direita
        o filho a direita tem um reatach no vô porque cai no remover recursivo que ja preve isto adicionando o nó a direita no temp e reatando temp a arvore"""
        """Interface pública para remoção."""
        self.raiz = self._remover_recursivo(self.raiz, numero)

    def _remover_recursivo(self, no_atual, numero):
        if no_atual is None:
            return no_atual

        if numero < no_atual.numero:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, numero)
        elif numero > no_atual.numero:
            no_atual.direita = self._remover_recursivo(no_atual.direita, numero)
        else:

            if no_atual.esquerda is None:
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                no_atual = None
                return temp


            temp = self._obter_menor_no(no_atual.direita)
            
            no_atual.numero = temp.numero
            
            no_atual.direita = self._remover_recursivo(no_atual.direita, temp.numero)

        if no_atual is None:
            return no_atual

        self._atualizar_altura(no_atual)

        balanceamento = self._fator_balanceamento(no_atual)

        if balanceamento > 1 and self._fator_balanceamento(no_atual.esquerda) >= 0:
            return self._rotacao_direita(no_atual)

        if balanceamento > 1 and self._fator_balanceamento(no_atual.esquerda) < 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if balanceamento < -1 and self._fator_balanceamento(no_atual.direita) <= 0:
            return self._rotacao_esquerda(no_atual)

        if balanceamento < -1 and self._fator_balanceamento(no_atual.direita) > 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual


    def exibir_estrutura(self):
        """Imprime a estrutura da árvore horizontalmente no terminal."""
        if self.raiz is None:
            print("Árvore vazia.")
        else:
            print("\n--- Estrutura Atual da AVL ---")
            self._exibir_estrutura_recursivo(self.raiz, "", True)
            print("-" * 30)

    def _exibir_estrutura_recursivo(self, no_atual, prefixo, eh_ultimo):
        if no_atual is not None:
            self._exibir_estrutura_recursivo(
                no_atual.direita, 
                prefixo + ("│   " if eh_ultimo else "    "), 
                False
            )
            fb = self._fator_balanceamento(no_atual)
            
            print(prefixo + ("└── " if eh_ultimo else "┌── ") + f"{no_atual.numero} [Alt:{no_atual.altura}, FB:{fb}]")
            
            self._exibir_estrutura_recursivo(
                no_atual.esquerda, 
                prefixo + ("    " if eh_ultimo else "│   "), 
                True
            )
