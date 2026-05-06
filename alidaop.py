#   mais um jogo que eu fiz com a ajuda de vídeo aula, nesse é o clássico jogo de pedra papel e tesoura, 
#   onde o código pede o usuario para selecionar uma das opções e o computador seleciona uma opção aleatória, 
#   depois o código compara as escolhas e determina o vencedor. O jogo continua até que o usuário decida sair digitando "sair".
import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if escolha_usuario == "sair":
            print("Obrigado por jogar! Até a próxima!")
            break
        if escolha_usuario not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        escolha_computador = random.choice(opcoes)
        print(f"O computador escolheu: {escolha_computador}")
        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
             (escolha_usuario == "papel" and escolha_computador == "pedra") or \
             (escolha_usuario == "tesoura" and escolha_computador == "papel"):
            print("Você venceu!")
            choice=input("deseja jogar novamente? (s/n): ").lower()
            if choice == "n":
                print("Obrigado por jogar! Até a próxima!")
                break
        else:
            print("O computador venceu!")
            choice=input("deseja jogar novamente? (s/n): ").lower()
            if choice == "n":
                print("Obrigado por jogar! Até a próxima!")
                break


jogar()