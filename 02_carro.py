import os
os.system("cls")

print("Dados sobre seu Carro")

nome_carro = input("Digite o nome do Carro: ")
valor_carro = float(input("Digite o valor o Carro: "))
comsumo_por_litro = float(input("Digite o consumo por litro: "))

print("----------------------------------------------------------------")
print(f"| Carro: {nome_carro}")
print("| Valor", valor_carro)
print(f"| Consumo por litro: {comsumo_por_litro}")
print("----------------------------------------------------------------")
