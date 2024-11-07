import random
import time
#create a bag with 10 marbles
#starting amount of money
# current money amount
#result of last round
#how many rounds
#last marble
# welcome user to game
# loop drawing marbles
    #how much was bet
    #draw marble
    # win or loss
    #calc win or loss/ result and new amount/purse
    #lose game if lose half of money
    #print results
# print final results

class marbel():
    def __init__(self):
        self.bag = dict()
        self.money = 100.0
        self.jogadas = dict()
        self.continuar = 's'
        self.tempo = time.sleep(2)
        self.bag['red'] = 6
        self.bag['green'] = 4 

    def jogo(self):

        tipos_disponiveis = list(self.bag.keys())
        quantidade_disponiveis = list(self.bag.values())
        while self.continuar == 's':
            print('jogo começando ...')
            print(f' bolas disponiveis {self.bag.items()}')
            self.tempo
            print(f'existem {sum(self.bag.values())} bolas no total')
            pagamento = self.bag['red'] / sum(self.bag.values()) + 1
            aposta = float(input(f'deseja apostar quanto ?  a casa paga {pagamento} na aposta ' ))
            float(input(f'voce não tem esse ouro...... seu saldo é{self.money}.... : ')) if aposta > self.money else print(f'sua aposta foi {aposta}')
            sorteio = random.choices(population = tipos_disponiveis, weights = quantidade_disponiveis, k =1)
            self.bag.update({'red': self.bag['red'] -1 }) if sorteio == 'red' else self.bag.update({'green': self.bag['green'] -1})
            self.money += (pagamento * aposta) if sorteio == list('green') else self.money - (pagamento * aposta)/2
            (self.bag)
            print(sorteio)
            print(f' seu saldo é .... {self.money}')
            if self.bag['red'] == 0 or self.bag['green'] == 0: 
                print('as bolas se esgotaram, o jogo acabou')
                break

            self.continuar = str(input('deseja ocntinuar ?  s/n  ->   ').lower())


  #  def choices(self, population, weights=None, *, cum_weights=None, k=1):

aposta = marbel()
aposta.jogo()


bag = dict()
bag['red'] = 4
bag['green'] = 6
# Sorteio com pesos baseados na quantidade de cada cor de bola
sorteio = random.choices(list(bag.keys()), weights=bag.values(), k=1)[0]

print(f"A bola sorteada foi: {sorteio}")

print(bag.items())