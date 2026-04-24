import os
os.system

print("calculadora de desconto")

produto = input("qual o produto? ")
quantidade = int(input("quantos? "))
preco_por_unidade = int(input("quanto custa cada unidade? "))

total = quantidade * preco_por_unidade
if quantidade <= 5 :
    desconto = total * 2 / 100
elif quantidade >= 5 and quantidade <= 10 :
    desconto = total * 3 / 100
else :
    desconto = total * 5 / 100

total_a_pagar = total - desconto

print(f"seu TOTAL e de {total:.2f}")
print(f"desconto: R${desconto:.2f}")
print(f"seu TOTAL A PAGAR {total_a_pagar:.2f}")
