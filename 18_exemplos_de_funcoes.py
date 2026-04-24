import os
os.system("cls")

print("Aula de Funções no Python")

#criando a funçâo escreva
def escreva():
    print("A função escreva executou!")

def cadastrar_usuario(usuario, senha, email, telefone):
    input("Pressione <Enter> para ...")
    print("Dados do usuario cadastrado")
    print(F"Usuário: {usuario}")
    print(F"E-mail: {email}")
    print(F"Senha: {senha}")
    print(F"Telefone: {telefone}")


#Chamando a funçâo escreva
escreva()


#Chamando a função cadastrar_usuario
print("Por favor, insira seus dados")
usuario = input("informe seu usuario:")
senha = input("informe seu senha:")
email = input("informe seu e-mail:")
telefone = input("informe seu telefone:")

cadastrar_usuario(usuario,senha,email,telefone)