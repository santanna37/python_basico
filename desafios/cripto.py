print('Project -  Crypto')
# create keys string
# autogenerate the values string by offsetting original string
# create two dictionaries
#user input 'the message' and mode
# run encode or decode
# return result
# clean and beautify the code 
codigo = [1, 14, 12, None, 3, 8, 0]
frase = 'bom dia'
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class cripto():
    def __init__(self):
        
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','',' ',None]
        self.cod = dict(index for index in enumerate(abc))
        self.descod = dict(zip(self.cod.values(), self.cod.keys()))
        self.texto_cripto = []
        self.texto_descrito = []
    def encrip(self,texto:str) ->list:
        texto = list(texto)
        #print(texto)
        for i in texto:
            try:
                #print(i)
                self.texto_cripto.append(self.descod.get(i))
                #print('code ',self.cod.items())
                #print('descode', self.descod.items())
                #print(self.texto_cripto)
                
            except Exception: 
                print('erro')
        print(self.texto_cripto)
    
    def descrip(self, criptografia:list):
        for i in criptografia:
            try:
                self.texto_descrito.append(self.cod.get(i))
            except Exception:
                print('erro')
                
        print(self.texto_descrito)

crip = cripto()
a = crip.encrip(texto=frase)
b = crip.descrip(criptografia=codigo)
print(a)
print(b)
# dicionario numero-letra
x = dict(index for index in enumerate(abc))
#print('isso é o X  ', x)

#dicionario letra numero
x2 = dict(zip(x.values(),x.keys()))
#print('isso é x2 ', x2)
#y = dict(key, value for key ,value in abc) 

# for o,e in x.items():
#     print(o, e)

#print(' isso é o Y ', y)

#separando em palavras 
#print(frase.split())


#separando na palavra
lista = list(frase)

#print(x.values())
a = str(lista[0])
#print(type)
#print(' teste  x', x.values())

#print(x2.get(f'{a}'))
x = list(i for i  in x2 if a == x2.keys())

#print(x)