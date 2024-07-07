# Crie um programa onde 4 jogadores recebam numeros aleatorios de um dado
# Guarde os resultados em um dicionarrio
# Ao final, ordene o dicionario, sabendo que o vencedor é o que tirou o maior numero do dados

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print(jogo)

## RESUTLADO EM LISTA
ranking = list()

print("Valores Sorteados: ")
print()
for k, v in jogo.items():
    print(f"{k} tirou {v} no dados.")
    sleep(1)

ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)   

print("Valores Ordenados: ")
print()
print(ranking) 
print()

for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")
    sleep(1)