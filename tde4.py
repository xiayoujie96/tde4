import random   #usado pra importar o randint, pra chamar um numero aleatorio

print("bem vindo, jogadores\n\nmodos de jogo")
print('(1)humano x humano')                     #display inicial
print('(2)humano x computador')
print('(3)Computador x computador')
total1 = 0              # aqui eu defino os valores dos totais pra 0, pra virarem uma variavel global e eu poder chamar elas nas funçõoes
total2 = 0
totalempate = 0
nome1 = ''              # mesma lógica das variaveis, defino elas pra um valor vazio, chamo nas funções e dentro delas eu defino os valores
nome2 = ''

def escolhas(total1, total2, totalempate, nome1, nome2, jogador1, jogador2):  #defino a lógica das escolhas, e chamo ela nas tres funções hxh, hxm e cxc
    print(f'O {nome1} escolheu o numero: {jogador1}')       #dentro do modo e das funções eu defino a variavel nome e jogador, ai eu importo elas aqui e chamo usando f string
    print(f'O {nome2} escolheu o numero: {jogador2}')
    if jogador1 == jogador2:
        print('Vocês empataram')
        totalempate += 1    # adiciona 1 pra variavel empate, e no final do codigo dou return pros valores serem atualizados
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        print(f'O {nome1} ganhou') # o codigo da linha 19 é a lógica de vitoria do j1
        total1 += 1
    else: 
        print(f'O {nome2} ganhou')
        total2 += 1
    return total1, total2, totalempate # atualização de valores

def hxh(total1, total2, totalempate, nome1, nome2):
    while True:
        jogador1 = int(input(f'Insira sua escolha, {nome1}: '))
        if jogador1 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        print('\n'*10)
        jogador2 = int(input(f'Insira sua escolha, {nome2}:  '))
        if jogador2 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        total1, total2, totalempate = escolhas(total1, total2, totalempate, nome1, nome2, jogador1, jogador2) # define os totais para o return do escolhas, ao mesmo tempo que chama a função escolhas()
        if parar(total1, total2, totalempate, nome1, nome2) == False:
            break
        hxh(total1, total2, totalempate, nome1, nome2)
    

def hxm(total1, total2, totalempate, nome1, nome2): 
    while True:
        jogador1 = int(input(f'Insira sua escolha, {nome1}: '))
        if jogador1 not in range(1, 4): 
            print('Você escolheu uma opção inválida. Tente de novo')
            continue
        jogador2 = random.randint(1, 3)
        total1, total2, totalempate = escolhas(total1, total2, totalempate, nome1, nome2, jogador1, jogador2)
        if parar(total1, total2, totalempate, nome1, nome2) == False:
            break
        hxm(total1, total2, totalempate, nome1, nome2)

def cxc(total1, total2, totalempate, nome1, nome2):
    while True:
        jogador1 = random.randint(1, 3)
        jogador2 = random.randint(1, 3)
        escolhas(total1, total2, totalempate, nome1, nome2, jogador1, jogador2)
        total1, total2, totalempate = escolhas(total1, total2, totalempate, nome1, nome2, jogador1, jogador2)
        if parar(total1, total2, totalempate, nome1, nome2) == False:
            break
        hxm(total1, total2, totalempate, nome1, nome2)

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
                                      
def modo(nome1, nome2):
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
        return modo(nome1, nome2)  
    
modo(nome1, nome2)
