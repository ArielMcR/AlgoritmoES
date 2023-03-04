
# Faça um Programa que mostre a mensagem "Alô mundo!" na tela.
def HelloWorld():
    print("Hello World")

# Faça um Programa e crie variáveis para armazenar seu nome e sobrenome (em variáveis diferentes). Apresente na tela uma mensagem de boas vindas com o nome e sobrenome do usuário.
# sua idade, seu peso, sua altura e sua data de nascimento
def apresetaNome():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite sua idade: "))
    peso = int(input("Digite sua peso: "))
    altura = float(input("Digite sua altura: "))
    dtnasc = input("Digite a data do seu nascimento: ")

    print(" Olá {} {} seja muito bem vindo ao nosso sistema. \n Os dados informados foram, idade: {}, peso: {}, altura: {}, dtnasc: {}".format(nome,sobrenome,idade,peso,altura,dtnasc))
def Num():
    numero= int(input("Digite um número: "))
    print("O antecessor do número {} é: {} e seu sucessor é: {}".format(numero,numero-1,numero+1))

Num()
# HelloWorld()
# apresetaNome()