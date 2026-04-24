import os
os.system("cls")

print("Calculadora de IMC")

peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:")) 

imc = peso / (altura * altura)

imc = round(imc, 1)
imc = float(imc)

if imc > 16.9:
    situacao = "Muito abaixo do peso"
elif imc >= 17 and imc <= 18.4:
    situacao = "Abaixo do peso"
elif imc >= 18.5 and imc <= 24.9:
    situacao = "Peso normal"
elif imc >= 25 and imc <= 29.9:
    situacao = "Acima do peso"
elif imc >= 30 and imc <= 34.9:
    situacao = "Obesidade grau I"
elif imc >= 35 and imc <= 40:
    situacao = "Obesidade grau II"
elif imc > 40:
    situacao = "Obesidade grau III"

print(f"seu IMC e de {imc}")
print(f"Sua situação: {situacao}")