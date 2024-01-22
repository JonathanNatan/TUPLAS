player1 = int(input('Digite um numero: '))
player2 = int(input('Digite outro numero: '))
player3 = int(input('Digite mais um numero: '))  #input para tupla
player4 = int(input('Digite outro numero: '))

contador_par = 0 #contador par
numeros = (player1, player2, player3, player4) #tupla com valores

numero_de_dois = numeros.count(9) #contador de quantas vezes 9 foi encontado

print(numeros)

print(f'O valor 9 apareceu {numero_de_dois} vezes')
if 3 in numeros: #se 3 estiver em numeros, o if vai acionar, se nao, nao 
    aparacer_valor = numeros.index(3)
    print(f'O valor 3 apareceu na posição {aparacer_valor+1}')
else:
    print('O valor 3 nao foi digitado')
 
for c in numeros: #loop para ver se a tupla tem par
    if c % 2 == 0:
        contador_par += 1
print(f'Foram encontrador {contador_par} pares nessa tupla')