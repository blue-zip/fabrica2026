import os
os.system("cls")

print("Exemplo - Tabuada com while")

numero = float(input("Informe um numero: "))

print(f" === TABUADA do {numero} ===")

contador = 0

while (contador <= 1000):
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1


