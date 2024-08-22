import random

print("bem vindo, jogadores\n\nmodos de jogo")
print('(1)humano x humano')
print('(2)humano x computador')
print('(3)Computador x computador')
total1 = 0
total2 = 0
totalempate = 0
escolha_modo = 0
nome1 = ''
nome2 = ''
def atualizar(total1, total2, totalempate, nome1, nome2, escolha_modo):
    while True:
        if escolha_modo == 3:
            jogador1 = random.randint(1, 3)
            jogador2 = random.randint(1, 3)
        if escolha_modo == 2:
            jogador2 = random.randint(1, 3)
            jogador1 = int(input(f'Insira sua escolha, {nome1}: '))
        else: 
            if jogador1 not in range(1, 4): 
                print('Você escolheu uma opção inválida. Tente de novo')
            continue
        print('\n'*10)
        jogador2 = int(input(f'Insira sua escolha, {nome2}:  '))
        if jogador2 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        if jogador1 == jogador2:
            print('Vocês empataram')
            totalempate += 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
            print(f'O {nome1} ganhou')
            total1 += 1
        else: 
            print(f'O {nome2} ganhou')
            total2 += 1
        if parar(total1, total2, totalempate, nome1, nome2) == False:
            break
    
def hxh(total1, total2, totalempate, nome1, nome2):
        atualizar(total1, total2, totalempate, nome1, nome2, escolha_modo)
        
def hxm(total1, total2, totalempate, nome1, nome2): 
        atualizar(total1, total2, totalempate, nome1, nome2, escolha_modo)

def cxc(total1, total2, totalempate, nome1, nome2):
        atualizar(total1, total2, totalempate, nome1, nome2, escolha_modo)
        
def parar(total1, total2, totalempate, nome1, nome2):
    while True:
        resposta = input('Deseja continuar? (S/N): ').lower()
        if resposta == 'n':
            if total1 > total2:
                print(f'O vencedor foi o {nome1}')
            elif total2 > total1:
                print(f'O vencedor foi o {nome2}')
            else: 
                print('O jogo empatou')
            print(f'O placar de vitórias do {nome1} é {total1}')
            print(f'O placar de vitórias do {nome2} é {total2}')
            print(f'O total de empates é {totalempate}')
            return False
        elif resposta == 's':
            return True
        else:
            print('Opção inválida. Tente novamente')     
                                      
def modo(nome1, nome2, escolha_modo):
    escolha_modo = int(input('Escolha o modo: '))
    print('As escolhas são: ')
    print('Pedra(1)')
    print('Papel(2)')
    print('Tesoura(3)')
    if escolha_modo == 1:
        nome1 = input('Insira o seu nome, jogador 1 :').title()
        nome2 = input('Insira o seu nome, jogador 2 :').title()
        hxh(total1, total2, totalempate, nome1, nome2)
    elif escolha_modo == 2:
        nome1 = input('Insira o seu nome, jogador 1 :').title()
        nome2 = 'Computador'
        hxm(total1, total2, totalempate, nome1, nome2) 
    elif escolha_modo == 3:
        nome1 = 'Computador 1'
        nome2 = 'Computador 2'
        cxc(total1, total2, totalempate, nome1, nome2)
    else:
        print('Escolha inválida. Tente novamente')
        return modo(nome1, nome2, escolha_modo)  
modo(nome1, nome2, escolha_modo)
