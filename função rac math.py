import matplotlib.pyplot as plt
import numpy as np

def funcX():
    while True:
        print('Insira o valor de A, B e Y')
        a = int(input('Valor de A(maior que 0): '))
        if a == 0:
            print('O valor de A não pode ser 0')
            continue
        b = int(input('Valor de B: '))
        y = int(input('Valor de Y: '))
        x = (y - b) / a
        print(f'O valor de X é {x}')
        return a, b, x
        
def plotar_funcao_primeiro_grau(a, b, x_min, x_max):
    x = np.linspace(x_min, x_max, 100)
    y = a * x + b
    plt.plot(x, y, label=f'y = {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da Função de Primeiro Grau')
    plt.legend()
    plt.grid(True)
    plt.show()
def funcY():
    while True:
        print('Insira o valor de A, B e X')
        a = int(input('Valor de A(maior que 0): '))
        if a == 0:
            print('O valor de A não pode ser 0')
            continue
        b = int(input('Valor de B: '))
        x = int(input('Valor de x: '))
        y = (a * x) + b
        print(f'O valor de Y é {y}')
        return a, b, x

def modo():
    while True:
        print('Você pode usar o algoritmo para encontrar X (1) ou Y (2). Deseja encontrar qual?')
        escolha_modo = input('Escolha: ')
        if escolha_modo == '1':
            a, b, x = funcX()
            plotar_funcao_primeiro_grau(a, b, x-10, x+10)
            break
        elif escolha_modo == '2':
            a, b, x = funcY()
            plotar_funcao_primeiro_grau(a, b, x-10, x+10)
            break
        else:
            print('Escolha inválida. Tente novamente')

modo()
