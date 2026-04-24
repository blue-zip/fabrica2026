import os 
os.system("cls")

print("Calculadora de Desconto")

nome_produto = input("Digite o nome do produto:")
preco = float(input("Informe o preço:"))
desconto = float(input("Informe percentual:"))

valor_do_desconto = (preco * desconto) / 100 

preco_final = preco - valor_do_desconto

print("--------------------------------------------")
print("-------------Relatorio de Vendas------------")
print(f"Perco do Produto R$ {preco:.2f}")
print(F"valor do desconto R$ {valor_do_desconto}")
print(f"Total com desconto R$ {preco_final}")