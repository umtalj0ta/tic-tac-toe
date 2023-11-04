import class_tabuleiro

from os import system, name

class GestaoJogo():
    def __init__(self):
        self.tabuleiro = class_tabuleiro.Tabuleiro("?")
        self.turno = 1

        self.tabuleiro.printTabuleiro()

        print(" Tic Tac Toe\n")
        print(" O Jogador 1 tem o simbolo -> O")
        print(" O Jogador 2 tem o simbolo -> X")
        print(" A posição vazia tem o simbolo -> ?")
        print("\n")

        while 1:
            self.jogador1()
            self.clear()
            self.tabuleiro.printTabuleiro()
            if self.tabuleiro.verificarLinhaorDiagonal("O"):
                print("Jogador 1 ganhou!")
                return
            elif not self.tabuleiro.verificarExisteCasasVazias():
                print("empate :( ")
                return

            self.jogador2()
            self.clear()
            self.tabuleiro.printTabuleiro()
            if self.tabuleiro.verificarLinhaorDiagonal("X"):
                print("Jogador 2 ganhou!")
                return
            elif not self.tabuleiro.verificarExisteCasasVazias():
                print("empate :( ")
                return

       

    def clear(self):
     
        # for windows
            if name == 'nt':
                _ = system('cls')
     
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
                
    def jogador1(self):
        print("Turno Jogador 1")
        self.turno = 1

        self.coluna_escolhida1 = int(input("Coluna [0-2]: "))
        self.linha_escolhida1 = int(input("Linha [0-2]: "))
        if self.coluna_escolhida1 > 2 or self.linha_escolhida1 > 2 or self.coluna_escolhida1 < 0 or self.linha_escolhida1 < 0:
            print("Cordenadas erradas. Valores entre 0 e 2")
            self.jogador2()
        elif not self.tabuleiro.verificarCasaVazia(self.coluna_escolhida1, self.linha_escolhida1):
            print("Jogada Invalida, escolher um casa vazia")
            self.jogador2()
        else:
            self.tabuleiro.setValorCasa(self.coluna_escolhida1, self.linha_escolhida1, "O")
        
            

    def jogador2(self):
        print("Turno Jogador 2")
        self.turno = 1

        self.coluna_escolhida1 = int(input("Coluna [0-2]: "))
        self.linha_escolhida1 = int(input("Linha [0-2]: "))
        if self.coluna_escolhida1 > 2 or self.linha_escolhida1 > 2 or self.coluna_escolhida1 < 0 or self.linha_escolhida1 < 0:
            print("Cordenadas erradas. Valores entre 0 e 2")
            self.jogador2()
        elif not self.tabuleiro.verificarCasaVazia(self.coluna_escolhida1, self.linha_escolhida1):
            print("Jogada Invalida, escolher um casa vazia")
            self.jogador2()
        else:
            self.tabuleiro.setValorCasa(self.coluna_escolhida1, self.linha_escolhida1, "X")
