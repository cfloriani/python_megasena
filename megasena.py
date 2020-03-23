import random
import os

i = 0
num_jogado = []
acertou = 0
sorteios = 0
acertos = [0,0,0,0,0,0,0]

while i <= 5:
    print('Jogada número ',i+1)
    num_jogado.insert(i,int(input('Informe o número da jogada: ')))
    while int(num_jogado[i]) < 1 or int(num_jogado[i]) > 60:
        num_jogado[i] = input('ERRO! Informe um número entre 1 e 60: ')   
    i += 1

while acertou != 6:
    acertou = 0
    num_sorteado = random.sample(range(1,60), 6)
    x = range(6)    
    for i in x:
        for j in x:
            if num_jogado[i] == num_sorteado[j]: 
                acertou += 1
    if acertou == 0: acertos[0] += 1
    elif acertou == 1: acertos[1] += 1
    elif acertou == 2: acertos[2] += 1
    elif acertou == 3: acertos[3] += 1
    elif acertou == 4: acertos[4] += 1
    elif acertou == 5: acertos[5] += 1
    elif acertou == 6: acertos[6] += 1
    sorteios += 1
    os.system('clear') 
    print('Você jogos os seguintes números')
    print(num_jogado)
    print('Os números sorteados foram')
    print(num_sorteado)
    print('Seu resultado')
    print('0: ',acertos[0])
    print('1: ',acertos[1])
    print('2: ',acertos[2])
    print('3: ',acertos[3])
    print('4: ',acertos[4])
    print('5: ',acertos[5])
    print('6: ',acertos[6])
    print('Qtd Sorteios ',sorteios)