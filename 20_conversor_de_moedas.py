import os
os.system("cls")

# Função que exibe o menu
def exibir_menu():
    print("=== Bem vindo ao conversor de Moedas ===")
    print("[1] - Converter DOLAR -> REAL")
    print("[2] - Convertor REAL -> DOLAR")
    print("[3] - sair do programa")

#Funçâo para converter de Dolar para real
def converter_dolar_para_real(quantia_dolar, cotacao):
    resultado = quantia_dolar * cotacao
    return resultado

#Funçâo para converter de Real para dolar
def converter_real_para_dolar(quantia_real, cotacao):
    resultado = quantia_real / cotacao
    return resultado
#Função para sair do programa
def sair():
    print("Muito obrigado por utilizar o programa")
    input("Pressione a tecla <enter> para sair")
    exit()



#Funçâo Principal do programa
def main(repetir):
    while repetir == "s":  
        exibir_menu()

        opcao = int(input("Escolha uma das opções:"))

        #Verifica qual foi a opção escolhida
        if (opcao == 1):
            cotacao = float(input("Informe a cotação do dolar ($):"))
            quantia_dolar = float(input("Informe a quantia em Dolares (USD):"))
            total_convertido = converter_dolar_para_real(quantia_dolar, cotacao)
            print(f"USD {quantia_dolar} = R$ {total_convertido}")
        elif (opcao == 2):
            cotacao = float(input("Informe a cotação do dolar ($):"))
            quantia_real = float(input("Informe a quantia em Reais (BRL):"))
            total_convertido = converter_real_para_dolar(quantia_real, cotacao)
            print(f"R$ {quantia_real} = $ {total_convertido}")
        elif (opcao == 3):
            sair()
        else:
            print("Opção invalida")

        repetir = input("Você gostaria de usar o programa de novo? [s]sim [n]não: ")

        os.system("cls")

#chamando a função main
main(repetir = "s")