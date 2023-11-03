import class_tabuleiro
import main
from os import system, name

class   GestaoJogo():

    def __init__(self):
        self.tabuleiro = class_tabuleiro.Tabuleiro("?")
        self.turno = 1
        
        self.linha_escolhida1 = 0
        self.coluna_escolhida1 = 0


        self.tabuleiro.printTabuleiro()
        
        print(" Tic Tac Toe\n")
        print(" O Jogador 1 tem o simbolo -> O")
        print(" O Jogador 2 tem o simbolo -> X")
        print(" A posição vazia tem o simbolo -> ?")
        print("\n")

        while 1 :
                self.jogador1()
                self.clear()
                self.tabuleiro.printTabuleiro()
                if self.tabuleiro.verificarExisteCasasVazias() == False:
                    print("empate :( ")
                    return

                self.jogador2()
                self.clear()
                self.tabuleiro.printTabuleiro()
                if self.tabuleiro.verificarExisteCasasVazias() == False:
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

        self.coluna_escolhida1 = int(input("Coluna[0-2]: "))
        self.linha_escolhida1 = int(input("Linha[0-2] : "))
        if self.coluna_escolhida1 > 2 or self.linha_escolhida1 > 2 or self.coluna_escolhida1 < 0 or self.coluna_escolhida1 < 0 and self.turno == 1:
            print("Cordenadas erradas. Valores entre 0 e 2")
            self.jogador1()
        self.verificarJogada1()
        self.tabuleiro.setValorCasa(self.coluna_escolhida1, self.linha_escolhida1,"O")
        self.tabuleiro.verificarLinhaorDiagonal("O")
        
        

    def verificarJogada1(self):
        if self.tabuleiro.getValorCasa( self.coluna_escolhida1, self.linha_escolhida1) == "X" and self.turno == 1:
            print("Jogada Invalida, escolher um casa vazia")
            self.jogador1() 

    def jogador2(self):
        print( "Turno Jogador 2") 
        self.turno = 2
        self.coluna_escolhida2 = int(input("Coluna: "))
        self.linha_escolhida2 = int(input("Linha : "))
        if self.coluna_escolhida2 > 2 or self.linha_escolhida2 > 2 or self.coluna_escolhida2 < 0 or self.coluna_escolhida2 < 0 != "X" and self.turno == 2:
            print("Cordenadas erradas. Valores entre 0 e 2")    
            self.jogador2()   
        self.verificarJogada2()
        self.tabuleiro.setValorCasa(self.coluna_escolhida2, self.linha_escolhida2,"X")
        self.tabuleiro.verificarLinhaorDiagonal("X")

    def verificarJogada2(self):
        if self.tabuleiro.getValorCasa( self.coluna_escolhida2, self.linha_escolhida2) == "O" and self.turno == 2:
            print("Jogada Invalida, escolher um casa vazia")
            self.jogador2() 


        