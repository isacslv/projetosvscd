# pequeno projeto baseado na brincadeira de adivinhação, onde o computador escolhe um número aleatório e o usuário tem que adivinhar qual é esse número.
# o programa deve fornecer feedback ao usuário se o palpite é muito baixo, muito alto ou correto, e contar o número de tentativas feitas pelo usuário.
# fiz esse projeto baseado em uma aula que vi no youtube, nele a professora ensinava a usar a biblioteca random, e ela passou essa atividade para praticar o uso dessa biblioteca.
import random

numero_escolhido=input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" \
"\nBem-vindo ao jogo de adivinhação! \n" \
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
"escolha o numero máximo para o jogo: ")

NUM=int(numero_escolhido)

def adivinha(x):
    num_secreto = random.randint(1, x)
    tentativas = 0
    while True:
        palpite = int(input(f"Digite um número entre 1 e {x}: "))
        tentativas += 1
        if palpite < num_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > num_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break
adivinha(NUM)
