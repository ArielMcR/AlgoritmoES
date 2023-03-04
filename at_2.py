
import math
import time

# Faça um programa que peça um número e apresente na tela o antecessor e o sucessor dele.
def Num():
    numero= int(input("Digite um número: "))
    print("O antecessor do número {} é: {} e seu sucessor é: {}".format(numero,numero-1,numero+1))

# Num()

# Faça um programa que peça dois números e imprima a soma deles.
def somar():
    numero1 = 1
    numero2 = 2
    print("A soma dos números {} e {} é de: {}".format(numero1,numero2,numero1+2))
# somar()

def multiplicar():
    numero1 = 12
    numero2 = 2
    print("A soma dos números {} e {} é de: {}".format(numero1,numero2,numero1*2))
# multiplicar()


# Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética.
def notaMedia():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota : "))
    nota3 = int(input("Digite a terceira nota : "))
    nota4 = int(input("Digite a quarta nota : "))
    média = nota1 + nota2 + nota3 + nota4 / 4
    print("A média das notas é: {}".format(média))
# notaMedia()

# Faça um programa que converta metros para centímetros.
def metrosParaCentrimetros():
    metros = int(input("Digite o valor em metros para ser convertido: "))
    print("O valor em centímetros é de: {}cm".format(metros*100))
# metrosParaCentrimetros()

# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
def areaCiruclo():
    raio = int(input("Digite o raio de um círculo: "))
    area = 3.14 * (math.pow(raio,2))
    print("Area circulo é de: {} cm²".format(area))
# areaCiruclo()

# Faça um programa que peça a medida do lado de um quadrado, calcule e mostre sua área. Em seguida, mostre também o perímetro do quadrado para o usuário.
def quadrado():
    lado = int(input("Digite o lado de um quadrado: "))
    area = math.pow(lado, 2)
    perimetro = lado * 4
    print("A area do quadrado é de: {} cm² \ne possui um perímetro de: {}cm²".format(area, perimetro))
# quadrado()

# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no dia. Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês (considerando 30 dias)
def horaganha():
    hora1 = float(input("Digite quando você ganha por 1 hora trabalhada: "))
    horasTrabalhadas = int(input("Digite o total de horas trabalhadas em um dia: "))
    valor1dia = hora1 * horasTrabalhadas / 1
    valor2dia = hora1 * (horasTrabalhadas*30) / 1
    print("Em um dia você ganha um total de: {} em {} horas trabalhadas"
     "\nem 30 dias você fatura um total de {} em {} horas trabalhadas".format(valor1dia, horasTrabalhadas, valor2dia, horasTrabalhadas*30))
# horaganha()

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

def conversaoTemp():
    Farenheit = float(input("Digite o valor da temperatura em Farenheit: "))
    celsius  = round(5*(Farenheit-32)/9,4)
    print("Calculando..... isso pode levar um tempo")
    time.sleep(3)
    print("Farenheit {} \nCelsius {}".format(Farenheit,celsius))
# conversaoTemp()


# Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²
def iMC():
    peso = int(input("Digite seu peso: "))
    altura = float(input("Digite a sua altura: "))
    imc = round(peso / math.pow(altura,2),3)
    print("Calculando seu imc.... isso pode levar um tempo")
    time.sleep(2)
    print("O seu IMC é de: {}".format(imc))
# iMC()

# Dada a equação: ax²+bx+c=0 peça para o usuário informar o valor de a, b e c e calcule
def funcaoSegundoGrau():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    if a == 0: 
        print("Informe um valor válido para A, por favor")
    raiz = b*b - 4*a*c
    x1 = round((-b + math.sqrt(abs(raiz))) / (2*a),3)
    x2 = round((-(b) - math.sqrt(abs(raiz))) / (2*a),2)
    print("A função {}² + {} + {} = 0, tem como raizes o valores.....".format(a,b,c))
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))

# funcaoSegundoGrau()
"""
Faça um programa em Python que receba o nome, o desconto (%) 
e o valor de um produto. Em seguida, apresente o nome, 
o valor atual, o desconto (em reais) e o valor final do produto da seguinte maneira 
"""
def produto():
    nome_Produto  = input("Digite o nome do produto: ")
    preco_Produto  = float(input("Digite o preço do produto: "))
    desconto = int(input("Digite o desconto em porcentagem: "))
    valor_Desconto = preco_Produto * desconto/100
    valor_final = preco_Produto - valor_Desconto
    print("Calculando o desconto.....")
    time.sleep(1.2)
    print("-------------------------------")
    print("Produto: {}".format(nome_Produto))
    print("-------------------------------")
    print("Valor: R${}".format(preco_Produto))
    print("Desconto: R${}%, dando um total de {}".format(desconto, valor_Desconto))
    print("-------------------------------")
    print("Valor Final: R${}".format(valor_final))

# produto()




"""
 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
 que custam R$120,00. O programa deve informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""
def pintura():
    metros_Pintar = float(input("Digite a quantidade em metros que você pintar: "))
    litro_1 = 54
    precoUmaLata = 120
    v1 = round(((metros_Pintar * precoUmaLata) / litro_1) / precoUmaLata,0)
    print("Calculando a quantidade de latas......")
    time.sleep(0.5)
    print("Você irá precisar de {} latas".format(v1))
# pintura()


"""
Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre 
o total do seu salário no referido mês
(salário bruto), sabendo-se que são descontados 7.5% 
para o Imposto de Renda, 8% para o INSS e 1% 
para o sindicato. Faça um programa que nos d
"""
def salarioBruto():
    hora1 = float(input("Digite quando você ganha por 1 hora trabalhada: "))
    horasTrabalhadas = int(input("Digite o total de horas trabalhadas em um mês: "))
    valorBruto = hora1 * horasTrabalhadas / 1
    impostoRenda = round(valorBruto * (7.5/100),2)
    inss = round(valorBruto * (8/100),2)
    sindicato = round(valorBruto * (1/100),2)
    dispesas = impostoRenda + inss + sindicato 
    valorLiquido = round(valorBruto - dispesas,2)
    print("+ Sálario Bruto R${}".format(valorBruto))
    print("- IR(7,5%) R${}".format(impostoRenda))
    print("- Inss(8%) R${}".format(inss))
    print("- Sindicato(1%) R${}".format(sindicato))
    print("= Sálario Liquido R${}".format(valorLiquido))
salarioBruto()

