print('Calculadora')
v1 = float(input('Insira um valor'))
v2 = float(input('Insira outro valor'))

def soma (a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b 
def mult(a,b):
    return a*b

while True: 
    op = input("Escolha uma operação [1]para somar,[2]para subtrair, [3]para multi,[4]para div,[0] para sair ")
    if op == '1':
    print('resultado da soma'soma)
    elif op == '2':
        res = sub(v1,v2)
    else: 
    print('Escolha invalida')
#fazer um programa que calcule sua nota anual da fiap#