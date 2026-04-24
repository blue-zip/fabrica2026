import os
os.system("cls")

#Etapa 01 - Realizar as entradas
print("Calculadora de Medias")

nome_do_aluno = input("Digite o nome do aluno:")

nota01 = float(input("Informe a nota do 1º Bimestre:"))
nota02 = float(input("Informe a Nota do 2º Bimestre:"))
nota03 = float(input("Informe a Nota do 3º Bimestre:"))
nota04 = float(input("Informe a Nota do 4º Bimestre:"))

#Etapa 02 - Processamento (Calculo)
media = (nota01 + nota02 + nota03 + nota04) / 4

#Etapa 03 - Saída (Resultado) 
if media >= 6 :
    print(f"sua media e {media} você foi aprovado ")
elif media >= 4 and media < 6 :
    print(f"sua media e {media} você vai para a recuperação")
else :
    print(f"sua media e {media} você sera retido")