
'''
settar o print pra explicar a brincadeira, e definir a escolha se vai ser hxh, hxm, mxm
pra fazer o humano x maquina e maquina x maquina, da pra usar randint, que vai fazer eles escolherem um numero aleatorio de 1 a 3

pro jogo ter infinitas rodadas, vamos ter que settar um função com while True: etc etc, e um elif input = 'parar': break, else: raise value error
algo assim^
eh importante a gente ter como esconder a escolha da primeira pessoa. acho que da pra fazer um
escolha1 = int(input('escolha))
print(\n*10)
'''
import random

print("bem vindo, jogador\n\nmodos de jogo")
print('(1)humano x humano')
print('(2)humano x computador')
print('(3)Computador x computador')
def hxh():
    print('Suas escolhas são: ')
    print('Pedra(1)')
    print('Papel(2)')
    print('Tesoura(3)')
    while True:
        jogador1 = int(input('Insira sua escolha, jogador 1: '))
        if jogador1 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        print('\n'*10)
        jogador2 = int(input('Insira sua escolha, jogador 2: '))
        if jogador2 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        if jogador1 == jogador2:
            print('Vocês empataram')
        elif jogador1 == 1 and jogador2 == 2:
            print('O jogador 2 ganhou')
        elif jogador1 == 2 and jogador2 ==3:
            print('O jogador 2 ganhou')
        elif jogador1 == 3 and jogador2 == 1:
            print('O jogador 2 ganhou ')
        else: 
            print('O jogador 1 ganhou')
        parar = input('Para parar o jogo, digite (4): ')
        if parar == '4':
            print('O jogo foi encerrado')
            break
def hxm(): 
    print('Suas escolhas são: ')
    print('Pedra(1)')
    print('Papel(2)')
    print('Tesoura(3)')
    while True:
        jogador1 = int(input('Insira sua escolha, jogador 1: '))
        if jogador1 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        jogador2 = random.randint(1, 3)
        print(f'O jogador 2 escolheu o numero: {jogador2}')
        if jogador1 == jogador2:
            print('Vocês empataram')
        elif jogador1 == 1 and jogador2 == 2:
            print('O jogador 2 ganhou')
        elif jogador1 == 2 and jogador2 ==3:
            print('O jogador 2 ganhou')
        elif jogador1 == 3 and jogador2 == 1:
            print('O jogador 2 ganhou ')
        else: 
            print('O jogador 1 ganhou')
        parar = input('Para parar o jogo, digite (4): ')
        if parar == '4':
            print('O jogo foi encerrado')
            break
def cxc():
    print('Suas escolhas são: ')
    print('Pedra(1)')
    print('Papel(2)')
    print('Tesoura(3)')
    while True:
        computador1 = random.randint(1, 3)
        computador2 = random.randint(1, 3)
        print(f'O computador 1 escolheu o numero: {computador1}')
        print(f'O computador 2 escolheu o numero: {computador2}')
        if computador1 == computador2:
            print('Vocês empataram')
        elif computador1 == 1 and computador2 == 2:
            print('O computador 2 ganhou')
        elif computador1 == 2 and computador2 ==3:
            print('O comutador 2 ganhou')
        elif computador1 == 3 and computador2 == 1:
            print('O comptador 2 ganhou ')
        else: 
            print('O computador 1 ganhou')
        parar = input('Para parar o jogo, digite (4): ')
        if parar == '4':
            print('O jogo foi encerrado')
            break


def modo():
    escolha_modo = int(input('Escolha o modo: '))
    if escolha_modo == 1:
        hxh()
    elif escolha_modo == 2:
        hxm() 
    elif escolha_modo ==3:
        cxc()
    else:
        print('Escolha inválida. Tente novamente')
        return modo()  
modo()
