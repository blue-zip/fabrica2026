import os 
os.system("cls")

#Etapa - entrada
print("Super Habilitação")
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))


if idade >= 18 :
    cnh = input("Você tem cnh? (Sim ou Não):")

    if cnh == "Sim":
        print("Você pode dirigir!")
    else:
        print("Voce não tem cnh, não pode")
    
else:{
    print("Não pode Dirigir!")
}
