import os
import random
import time
os.system("cls")

nome = input("Insira seu nome:")


print("Escolha sua arma: ")
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

#Verificando quem ganhou
#Caso o jogador escolha a pedra
if opcao_jogador == "Pedra" and opcao_maquina == "Papel":
    print("Papel vence Pedra ")
    print("O computador venceu")
elif opcao_jogador == "Pedra" and opcao_maquina == "Tesoura":
    print("Pedra vence tesoura")
    print("Você venceu")
#Caso o jogador escolha o papel    
elif opcao_jogador == "Papel" and opcao_maquina == "Tesoura":
    print("Tesoura vence Papel")
    print("O computador venceu")
elif opcao_jogador == "Papel" and opcao_maquina == "Pedra":
    print("Papel vence pedra")
    print("Você venceu")
#Caso o jogador escolha tesoura     
elif opcao_jogador == "Tesoura" and opcao_maquina == "Pedra":
    print("Pedra vence tesoura")
    print("O computador venceu")
elif opcao_jogador == "Tesoura" and opcao_maquina == "Papel":
    print("Tesoura vence papel")
    print("Você venceu")
#Caso o jogador e a maquina escolham a mesma coisa
elif opcao_jogador == opcao_maquina: 
    print("Você e o computador escolheram a mesma arma")
    print("empate")
#Caso o jogador não escolha uma arma
else:
    print("Você não escolheu uma arma")
    print("O computador venceu por desistencia")

