import os
os.system("cls") 

print("Calculadora")

nome = input("Informe o seu nome:")
numero01 = float(input("Informe o primeiro número: "))
numero02 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação(+ - * / ): ")

if operacao == "+" :
    print(f"o resultado e {numero01 + numero02}")
elif operacao == "-" :
    print(f"o resultado e {numero01 - numero02}")
elif operacao == "*" :
    print(f"o resultado e {numero01 * numero02}")
elif operacao == "/" :
    print(f"o resultado e {numero01 / numero02}")
else :
    print("ESCOLHA UMA OPERAÇÃO!")
