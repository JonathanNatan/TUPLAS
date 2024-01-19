numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
extenso = ('zero','um','dois','tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
player = None
while True:
    player = int(input('Digite um numero entre (0,20) Digite [999] parar: '))
    
    if player == 999:
        print('Voce terminou o programa!')
        break
    if not 0 <= player <= 20:
        print('Tente novamente, este numero nao existe')
        continue
    print(extenso[player])
