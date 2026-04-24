import os
os.system("cls")

print("Calculadora de Salario")

nome_professor = input("Informe o nome do professor: ")
aulas_semana = int(input("Informe quantas aulas ele deu essa semana: "))
nivel_do_professor = int(input("Informe o nivel do professor: "))
if nivel_do_professor == 1:
    salario_semana = aulas_semana * 12 
elif nivel_do_professor == 2:
    salario_semana = aulas_semana * 17
elif nivel_do_professor == 3:
    salario_semana = aulas_semana * 25
else:
    print("Esse nivel não existe")

print(f"O salario do professor e R${salario_semana:.2f}")