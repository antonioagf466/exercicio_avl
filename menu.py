from arvore import ArvoreAVL


class Menu:
    def __init__(self):
        self.arvore = ArvoreAVL()

    def exibir_menu(self):
        while True:
            print("\n" + "="*40)
            print("           MENU ÁRVORE AVL")
            print("="*40)
            print(" [1] Inserir número")
            print(" [2] Remover número")
            print(" [3] Buscar número")
            print(" [4] Ver estatísticas (Altura, Nós...)")
            print(" [5] Exibir estrutura gráfica")
            print(" [0] Sair")
            print("="*40)

            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                try:
                    num = int(input("Digite o número para inserir: "))
                    self.arvore.inserir(num)
                    print(f"\nSucesso: {num} processado.")
                    self.arvore.exibir_estrutura()  
                except ValueError:
                    print("Erro: Digite apenas números inteiros.")
    
            elif opcao == "2":
                try:
                    num = int(input("Digite o número para remover: "))
                    if self.arvore.buscar(num):
                        self.arvore.remover(num)
                        print(f"\nSucesso: {num} removido.")
                        self.arvore.exibir_estrutura()  
                    else:
                        print(f"Aviso: Número {num} não encontrado na árvore.")
                except ValueError:
                    print("Erro: Digite apenas números inteiros.")
    
            elif opcao == "3":
                try:
                    num = int(input("Digite o número para buscar: "))
                    no = self.arvore.buscar(num)
                    if no:
                        fb = self.arvore._fator_balanceamento(no)
                        print(f"Encontrado! Nó {num} -> Altura: {no.altura}, Fator de Balanceamento: {fb}")
                    else:
                        print(f"O número {num} NÃO está na árvore.")
                except ValueError:
                    print("Erro: Digite apenas números inteiros.")
    
            elif opcao == "4":
                print("\n--- Estatísticas da Árvore ---")
                print(f"Altura da raiz: {self.arvore.calcular_altura()}")
                print(f"Total de nós  : {self.arvore.contar_nos()}")
                print(f"Total de folhas: {self.arvore.contar_folhas()}")
    
            elif opcao == "5":
                self.arvore.exibir_estrutura()
    
            elif opcao == "0":
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")

