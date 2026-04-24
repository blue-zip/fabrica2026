import os
os.system("cls")

print("Super termometro")

temperatura = float(input("Qual a temperatura?"))

if temperatura >= 25: 
    print("Está Quente!")

elif temperatura >= 15 and temperatura <= 24: 
    print("Temperatura agradavel")
 
else: {
    print("Está Frio!")
}  