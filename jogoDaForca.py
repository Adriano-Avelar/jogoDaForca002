import random
from os import system, name 

#função limpa a tela de execução
def limpa_tela():
    #windows
    if name =='nt':
        _=system('cls')
    #mac ou linux
    else:
        _=system('clear')
#board 
board = ['''
>>>>>>>>Hangman<<<<<<<<
         
 +---+         
 |   |    
     |    
     |    
     |    
     |
 =========''','''             
 +---+         
 |   |    
 o   |    
     |    
     |    
     |
 =========''','''             
 +---+         
 |   |    
 o   |    
 |   |    
     |    
     |
 =========''','''                      
 +---+         
 |   |    
 o   |    
/|   |    
     |    
     |
 =========''','''                          
 +---+         
 |   |    
 o   |    
/|\  |    
     |    
     |
 =========''','''             
 +---+         
 |   |    
 o   |    
/|\  |    
/    |    
     |
 =========''','''             
 +---+         
 |   |    
 o   |    
/|\  |    
/ \  |    
     |
 =========''','''             

''']
#class
class Hangman:
    #metodo contrutor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []
    #metodo para adivinhar as letras 
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        
        else:
            return False
        return True
    
    #metodo para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
        
    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False
    #metodo para não mostra a letra board
    def hide_palavra(self):
        rtn =''
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    #metodo para checar o status do game e imprimir o board na tela.
    def print_game_status(self):

        print(board[len(self.letras_erradas)])
        print('\nPalavra:' + self.hide_palavra())
        print('\nLetras erradas:',)
        for letra in self.letras_escolhidas:
            print(letra,)
        print()
#Método para ter uma palavra d forma aleatória do banco de palavras
def rand_palavra():
    #lista de palavras
    palavras = ['banana','manga','bacuri','murucí','bacaba','taperebá','cupuaçu','castanha']
    #escolher randoricamente uma palavra
    palavra = random.choice(palavras)
    return palavra
#Método Main - execução do programa
def main():
    limpa_tela()
    #criar o objeto e selecinar uma palavra randomicamente
    game = Hangman(rand_palavra())
    
    while not game.hangman_over():
        #status do game
        game.print_game_status()
        #recebe input do terminal
        user_input = input ('\ndigite uma letra:')
        #verifica se a letra digitada faz parte da palavra
        game.guess(user_input)
    #verifica status do jogo
    game.print_game_status()
    
    #De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\n palabens! você venceu!')
    else:
        print('\ngame over! você perdeu.')
        print('a palavra era ' + game.palavra)
    print('\nFoi bom jogar com você! Agora vá estudar\n')
#executar o programar
if __name__ == '__main__':
    main()
    