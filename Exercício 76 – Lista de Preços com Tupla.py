# Definição da tupla 'lista' com produtos e preços alternados
lista = ('Lapis', 1.75,
        'Borracha', 2,
        'Caderno', 15.50,
        'Estojo', 25,
        'Compasso', 9.99,
        'Mochila', 120.32)

# Linhas de impressão para criar uma barra de separação antes e depois do título
print('-' * 40)
print(f'{"Listagem de Preços":^40}')  # Título centralizado na tela
print('-' * 40)

# Loop for para percorrer a tupla 'lista'
for pos in range(0, len(lista)):
    # Se o índice (pos) for par, imprime o nome do produto alinhado à esquerda com pontos e espaços
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        # Se o índice for ímpar, imprime o preço do produto formatado como um valor monetário
        print(f'R${lista[pos]:>7.2f}')
