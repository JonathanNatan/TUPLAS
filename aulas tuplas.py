lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#tuplas sao imutaveis
print(sorted(lanche)) #deixa em ordem

for c in lanche:
    print(f'Eu vou comer {c}')

for c in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[c]} na posição {c}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')

a = (1,2,3,5)
b = (3,1,3,45,5)
c = b + a
print(c.count(5)) #mostrar quantas vezes aparece esse numero
print(len(c))
print(c.index(45)) #achar qual posicao o numero ta. usar c.index(3, 1) para começar do 1 numero
