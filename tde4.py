import random

print("bem vindo, jogador\n\nmodos de jogo")
print('(1)humano x humano')
print('(2)humano x computador')
print('(3)Computador x computador')
total1 = 0
total2 = 0
totalempate = 0
def hxh(total1, total2, totalempate):
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
            totalempate += 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
            print('O jogador 1 ganhou')
            total1 += 1
        else: 
            print('O jogador 2 ganhou')
            total2 += 1
        if parar(total1, total2, totalempate) == False:
            break
        
def hxm(total1, total2, totalempate): 
    while True:
        jogador1 = int(input('Insira sua escolha, jogador 1: '))
        if jogador1 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        jogador2 = random.randint(1, 3)
        print(f'O jogador 2 escolheu o numero: {jogador2}')
        if jogador1 == jogador2:
            print('Vocês empataram')
            totalempate += 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
            print('O jogador 1 ganhou')
            total1 += 1
        else: 
            print('O jogador 2 ganhou')
            total2 += 1
        if parar(total1, total2, totalempate) == False:
            break

def cxc(total1, total2, totalempate):
    while True:
        jogador1 = random.randint(1, 3)
        jogador2 = random.randint(1, 3)
        print(f'O jogador 1 escolheu o numero: {jogador1}')
        print(f'O jogador 2 escolheu o numero: {jogador2}')
        if jogador1 == jogador2:
            print('Vocês empataram')
            totalempate += 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
            print('O jogador 1 ganhou')
            total1 += 1
        else: 
            print('O jogador 2 ganhou')
            total2 += 1
        if parar(total1, total2, totalempate) == False:
            break
        
def parar(total1, total2, totalempate):
    while True:
        resposta = input('Deseja continuar? (S/N): ').lower()
        if resposta == 'n':
            if total1 > total2:
                print('O vencedor foi o jogador 1')
            elif total2 > total1:
                print('O vencedor foi o jogador 2')
            else: 
                print('O jogo empatou')
            print(f'O placar de vitórias do jogador 1 é {total1}')
            print(f'O placar de vitórias do jogador 2 é {total2}')
            print(f'O total de empates é {totalempate}')
            return False
        elif resposta == 's':
            return True
        else:
            print('Opção inválida. Tente novamente')     
                                      
def modo():
    escolha_modo = int(input('Escolha o modo: '))
    print('As escolhas são: ')
    print('Pedra(1)')
    print('Papel(2)')
    print('Tesoura(3)')
    if escolha_modo == 1:
        hxh(total1, total2, totalempate)
    elif escolha_modo == 2:
        hxm(total1, total2, totalempate) 
    elif escolha_modo == 3:
        cxc(total1, total2, totalempate)
    else:
        print('Escolha inválida. Tente novamente')
        return modo()  
modo()
