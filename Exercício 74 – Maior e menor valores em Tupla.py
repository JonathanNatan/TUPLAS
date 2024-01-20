import random

numeros = (0,1,2,3,4,5,6,7,8,9,10) #TUPLA

numeros_aleatorios = random.sample(numeros, k=6) #ALEATORIO SEM PEGAR NUMEROS REPETIDOS 

print(numeros_aleatorios)

maior_num = max(numeros_aleatorios) #PEGAR MAIOR NUMERO COM O MAX

print(f'Maior numero {maior_num}')

menor_num = min(numeros_aleatorios) #PEGAR MENOR NUMERO COM MIN

print(f'Menor numero {menor_num}')


#USANDO RANDOM.SAMPLE SO VAI PEGAR NUMEROS SEM REPETIÇÃO, RANDOM.SAMPLE(NUMEROS, K=6) VAI PEGAR NUMEROS UNICOS SEM REPETIÇÃO NUMERO = LISTA/TUPLA E K = 6 É QUANTOS INDIVIDUOS VAI APARECER NA TELA


#USANDO RANDOM.CHOICES VAI PEGAR NUMEROS REPETIDOS, RANDOM.CHOICES(NUMEROS, K = 6) VAI FAZER A MESMA COISA DO SAMPLE SO QUE COM REPETIÇÕES