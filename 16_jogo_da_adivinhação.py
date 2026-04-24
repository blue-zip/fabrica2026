import os
import random
os.system("cls")

print("Bem vindo ao jogo da advinhação!")

nome = input("Digite o seu nome: ")

numero_secreto = random.randint(1,15)


jogar_de_novo = "sim"
tentativas = 0
numero_jogador = 0


while (jogar_de_novo == "sim"):
    while (tentativas <= 5):
        os.system("cls")

        tentativas += 1
        
        #Apenas para debug
        print(numero_secreto)

        numero_jogador = int(input("Digite um número de 1 a 15: "))

        if (numero_jogador > 15 or numero_jogador < 1):
            print("Você tem que digitar um numero de 1 a 15")
        elif (numero_jogador == numero_secreto):
            print("Você acertou")
            break
        elif (numero_jogador > numero_secreto):
            print("Você errou, o numero secreto e menor ")
        elif (numero_jogador < numero_secreto):
            print("Você errou, o numero secreto e maior")

        input(f"Tentativas {tentativas}")
        input("Pressione <enter> para tentar novamente...")

        

    print("Fim de jogo!")
    print(f"Você utilizou {tentativas} tentativas")
    jogar_de_novo = input("quer jogar de novo [sim] [não]: ")