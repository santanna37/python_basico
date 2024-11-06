import random 
import time

base_cidade = {'vida': 100,
                'atq': 10,
                'ouro':100
                }

tropas = {'vida':2,
          'atq': 1,
          'quant': 1
          }

class jogo():
    def __init__(self, cidade: dict, tropas: dict):
        self.cidade = cidade
        self.tropas = tropas
        self.cidade['vida'] = 90
        self.total_ataque_tropas = self.tropas['quant'] * self.tropas['atq']
        self.ataque_cidade = self.cidade['atq']
        self.quantidade_tropas_atacadas = self.ataque_cidade/5 
        self.atualizar = jogo.dano(self)
        print('o jogo começou')


        

    def dano(self):
        self.tropas.update({'quant': self.tropas['quant'] - self.quantidade_tropas_atacadas})
        self.cidade.update({'vida' : self.cidade['vida'] - self.total_ataque_tropas})
        self.tropas.update({'vida': self.tropas['vida'] - self.ataque_cidade})
        print(self.cidade['vida'])
        
    def rodada(self):
        
        for x in range(0,3):
            print(f'seus status atuais são:  {self.cidade.items()}')
            print('===================================================')
            time.sleep(2)
            print('Dado bonus ou onus - escolha par ou impar , o valor do dado será somado ou diminuido dos valores de ataque da sua cidade')
            dado_centro = random.randint(1,6) 
            print(dado_centro)
            print('=====================')
            time.sleep(2)
            self.cidade.update({'atq': self.cidade['atq'] + dado_centro})
            print(self.cidade.items())
            print('==========================================')
            time.sleep(2)
            print('rodada das tropas')
            time.sleep(1)
            dado_tropa = random.randint(1,3)
            print(f'as tropas essa tem um acrecimo de {dado_tropa}')
            self.tropas.update({'quant': self.tropas['quant'] + dado_tropa})
            print('as tropas tambem recebem acumulo no ataque')
            dado_tropa_quant = random.randint(1,6)
            print(f'o dano foi aumentado em: {dado_tropa_quant}')
            self.tropas.update({'quant': self.tropas['quant'] + dado_tropa_quant})
            print(self.tropas.items())
            # ataque 
            print(f' o centro matou {self.quantidade_tropas_atacadas}')
            #print
            self.tropas.update({'quant': self.tropas['quant'] - self.quantidade_tropas_atacadas})
            self.atualizar
            print(f" a quantidade de tropas atacantes é  {self.tropas['quant']}  com o dano de {self.total_ataque_tropas}")
            print('==================')
            time.sleep(2)
            # fase de atualizaçao 
            print(f'dano recebeu : {self.total_ataque_tropas}')
            self.cidade.update({'vida': self.cidade['vida'] - self.total_ataque_tropas})
            print(f' status centro: {self.cidade.items()}')
        print(self.total_ataque_tropas)
    

jogo(cidade=base_cidade,tropas=tropas).rodada()