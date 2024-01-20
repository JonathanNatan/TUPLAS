c1 = 0
c2 = 0
c3 = 0
times_nba = ('Celtics', 'Bucks', '76ers','Cavaliers','Knicks',
            'Heat','Peacers','Magic','Bulls','Hawks','Nets',
            'Raptors','Hornets','Wizards', 'Pistions')

for times in times_nba[:5]:

    c1 += 1 
    print(f'Os {c1} primeiros da tabela da NBA sao: {times}') 

for times in times_nba[-4:]:
    print(f'Os ultimos 4 colocados sao: {times}')
    c2 += 1

print(f'Os times em ordem alfabetica seriam: {sorted(times_nba)}')

print(f'O Heat esta na posição: {times_nba.index("Heat")+1}')