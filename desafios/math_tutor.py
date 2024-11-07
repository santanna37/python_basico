# desafio do tutor de matematica 
import random
import time

class Tutor():
    def __init__(self):
        self.pontos = dict()
        self.contas = dict()
        self.descanso2 = time.sleep(2)
        self.dicionarios()
        
    def dicionarios(self):
        self.pontos['pontos_ganhos'] = 0
        #self.contas[] 

    def soma(self):
        print('calculos de soma')
        contas = int(input(' quantas contas voce quer fazer ?  '))
        self.descanso2
        for rodadas in range(1,contas):
            print('=========')
            print('cada ponto certo vale 1 ponto')
            a = int(random.randint(1,10))
            b = int(random.randint(1,10))
            self.descanso2
            print(f' conta numero {rodadas} : {a} + {b}')
            resposta = int(input(' qual é a resposta ? '))
            
            if resposta == a+b: 
                self.pontos.update({'pontos_disputados' : rodadas, 'pontos_ganhos': self.pontos['pontos_ganhos'] +1 })
                self.contas[f'rodada_{rodadas}'] = ({f'conta_{rodadas}' : f'{a} + {b}', 'reposta_usuario': resposta, 'resposta_sistema': a + b})
                print(self.contas)
                print(self.pontos)
            elif resposta != a+b: 
                self.contas[f'rodada_{rodadas}'] = ({f'conta_{rodadas}' : f'{a} + {b}', 'reposta_usuario': resposta, 'resposta_sistema': a + b})
                print(self.contas)
                print(self.pontos)

aula = Tutor()

aula.soma()
