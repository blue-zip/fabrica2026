import os
os.system("cls")


def somar(numero1,numero2): 
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1,numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    return resultado

def dividir(numero1,numero2):
    resultado = numero1 / numero2
    return resultado

def exibir_opcoes():
    print("Escolha uma opção")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")

print("Seja Bem vindo a calculadora 3.0")

numero1 = float(input("Informe o primeiro número:"))
numero2 = float(input("Informe o segundo número:"))



op = input("Informe a operação:")

if op == "1":
    total = somar(numero1,numero2)
    print(f"seu resultado e {total}")
elif op == "2":
    total = subtrair(numero1,numero2,)
    print(f"seu resultado e {total}")
elif op == "3":
    total = multiplicar(numero1,numero2,)
    print(f"seu resultado e {total}")
elif op == "4":
    total = dividir(numero1,numero2,)
    print(f"seu resultado e {total}")
else:
    print(f"Esta opçâo não existe")

