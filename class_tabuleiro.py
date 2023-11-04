class Tabuleiro():
    
    def __init__(self, simbolo_vazio):
        self.casas = [simbolo_vazio] * 9
        self.simbolo_vazio = simbolo_vazio


    def getValorCasa(self, coluna, linha):
        return self.casas[coluna + (linha * 3)]

    def setValorCasa(self, coluna, linha, simbolo):
        if self.casas[coluna + (linha * 3)] == self.simbolo_vazio:
            self.casas[coluna + (linha * 3)] = simbolo
            return True
        else:
            return False

    def verificarCasaVazia(self,coluna,linha):
        if self.casas[coluna + (linha * 3)] == "?":
            return True

    def verificarExisteCasasVazias(self):
            i = 0
            while i <= 8 :
                if self.casas[i] == "?":
                    return True
                i += 1
            return False
    
    def printTabuleiro(self):
        print(f" {self.casas[0]} | {self.casas[1]} | {self.casas[2]} ")
        print("---+---+---")
        print(f" {self.casas[3]} | {self.casas[4]} | {self.casas[5]} ")
        print("---+---+---")
        print(f" {self.casas[6]} | {self.casas[7]} | {self.casas[8]} ")



    def verificarLinhaorDiagonal(self, simbolo):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for condition in win_conditions:
                if self.casas[condition[0]] == self.casas[condition[1]] == self.casas[condition[2]] == simbolo:
                    return True
        return False
            

            
 



