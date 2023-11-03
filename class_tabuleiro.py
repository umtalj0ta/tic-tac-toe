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
        
    def verificarLinhaorDiagonal(self,simbolo):
        if (self.casas[0] and self.casas[1] and self.casas[2]) == simbolo:
            return True
        
        elif (self.casas[3] and self.casas[4] and self.casas[5]) == simbolo:
            return True
        
        elif (self.casas[6] and self.casas[7] and self.casas[8]) == simbolo:
            return True
        
        elif (self.casas[0] and self.casas[3] and self.casas[6]) == simbolo:
            return True
        
        elif (self.casas[1] and self.casas[4] and self.casas[7]) == simbolo:
            return True
        
        elif (self.casas[2] and self.casas[5] and self.casas[8]) == simbolo:
            return True
        
        elif (self.casas[0] and self.casas[4] and self.casas[8]) == simbolo:
            return True
        
        elif (self.casas[2] and self.casas[4] and self.casas[6]) == simbolo:
            return True
        
        else:
            return False
            
    def verificarCasaVazia(self,coluna,linha):
        if self.casas[coluna + (linha * 3)] == "?":
            return True



    def printTabuleiro(self):
        print(f" {self.casas[0]} | {self.casas[1]} | {self.casas[2]} ")
        print("---+---+---")
        print(f" {self.casas[3]} | {self.casas[4]} | {self.casas[5]} ")
        print("---+---+---")
        print(f" {self.casas[6]} | {self.casas[7]} | {self.casas[8]} ")

    def verificarExisteCasasVazias(self):
            i = 0
            while i <= 8 :
                if self.casas[i] == "?":
                    return True
                i += 1
            return False

            
 



