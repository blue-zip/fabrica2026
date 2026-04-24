import os
import time
import random
os.system("cls")

print("Seja bem vindo ao pedra, papel e tesoura 2.0")

vida_jogador = 100
vida_computador = 100

nome = input("Informe o seu nome:")

print("Escolha a sua arma")
print("[1] - Pedra")
print("[2] - Papel")
print("[3] - Tesoura")

opcao_jogador = int(input("Escolha sua arma: "))

opcao_maquina = random.randint(1,3)

os.system("cls")

if opcao_jogador == 1:
    opcao_jogador = "Pedra"
    print("Você escolheu a Pedra")
elif opcao_jogador == 2:
    opcao_jogador = "Papel"
    print("Você escolheu o Papel")
elif opcao_jogador == 3:
    opcao_jogador = "Tesoura"
    print("Você escolheu a Tesoura")
else:
    print("A arma que voce escolheu não existe")

print("Aguarde o computador escolher uma arma...")

time.sleep(4)

if opcao_maquina == 1:
    opcao_maquina = "Pedra"
    print("O computador escolheu a Pedra")
elif opcao_maquina == 2:
    opcao_maquina = "Papel"
    print("O computador escolheu o Papel")
elif opcao_maquina == 3:
    opcao_maquina = "Tesoura"
    print("O computador escolheu a Tesoura")

input("Pressione <enter> para iniciar a batalha...")

os.system("cls")

while (vida_jogador > 0 and vida_computador > 0):

    os.system("cls")

    print(f"Seu HP: {vida_jogador}")
    print(f"HP do computador {vida_computador}")

    print("=== menu ===")
    print("[1] - Atacar")
    print("[2] - Curar")
    print("[3] - Fugir")

    jogador = int(input("O que você escolhe?: "))

    if (jogador == 1):
        print("Você atacou!")
        vida_computador -= 15
    elif (jogador == 2):
        print("Você se curou!")
        vida_jogador += 7
    elif (jogador == 3):
        print("Você fugiu...")
        break
    else :
        print("Você escolheu uma opçâo inválida!") 
    
    
    

    #O computador escolhe (Atacar, curar ou Fugir)
    computador = random.randint(1,3)

    if (computador == 1):
        print("O computador atacou!")
        vida_jogador -= 15
    elif (computador == 2):
        print("O computador se curou!")
        vida_computador += 7
    elif (computador == 3):
        print("O computador fugiu...")
        break
    
    time.sleep(3)
    os.system("cls")

input("pressione <enter> para verificar quem venceu...")

if (vida_jogador > vida_computador):
    print("Você ganhou!")
else:
    print("O computador venceu :(")

print("Fim de jogo!")