import os
os.system("cls")

print("Descubra se e par ou impar")

numero01 = int(input("Informe um numero: "))

if (numero01 % 2) == 0 :
    print("Este numero e par")
else :
    print("Este numero não e par")