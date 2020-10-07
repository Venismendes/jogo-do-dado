import random

pontos_jogador1 = 1000
pontos_jogador2 = 1000
dado = (1, 2, 3, 4, 5, 6)
jogadores = 1

jogador = input('Olá qual o seu nome: ')
print(f'Bem vindo ao jogo do dado {jogador}')


quantidade_jogadores = input('Deseja jogador de 2 jogadores? [S/N]: ').upper()


if quantidade_jogadores == 'S':
    jogadores = 2
    jogador1 = jogador
    jogador2 = input('Nome do segundo jogador: ')


print('=' * 40)
while jogadores == 1:
    print('Inicialmente você tem 1000 pontos!')
    print('[S] para sair!')
    print('[P] para ver seus pontos')
    print('[J] para jogar: ')
    while True:
        print('=' * 30)
        opcao = input('Opção: ').upper()
        print('=' * 30)

        while True:
            menu = True
            na = random.choice(dado)
            if na <= 3:
                valor = 'L'
            else:
                valor = 'H'

            if opcao == 'J':
                while True:
                    try:
                        if pontos_jogador1 <= 0:
                            print('Fim do jogo!!')
                            exit()
                        aposta = int(input('Quantos pontos: '))
                        if aposta <= 0 or aposta > pontos_jogador1:
                            print(f'O valor deve ser maior que 0, seus pontos são {pontos_jogador1}: ')

                        else:
                            low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            break
                    except ValueError:
                        print('valor inválido, digite apenas números inteiros.')
                
                
                while low_high != 'H' and low_high != 'L' and low_high != 'S':
                    print('Valor inválido')
                    low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                
                if low_high == valor and (low_high == 'L' or low_high == 'H'):
                    print(f'Você acertou e ganhou {aposta} pontos!!')
                    pontos_jogador1 = pontos_jogador1 + aposta
                    menu = False
                elif low_high == 'L' or low_high == 'H':
                    print(f'Você errou e perdeu {aposta} pontos!!')
                    pontos_jogador1 = pontos_jogador1 - aposta
                    menu = False
                    
                if low_high == 'S':
                    menu = True
                    break
                 
                print()
                print(f'Dado: {na} = {valor}')

                print(f'Seus pontos: {pontos_jogador1}')
                print('=' * 30)

            if opcao == 'S':
                exit()
            if opcao == 'P':
                print(f'Você possui {pontos_jogador1} pontos.')

            if menu == True:
                print('=' * 30)
                opcao = input('Opção: ').upper()
                print('=' * 30)
print('=' * 40)
while jogadores == 2:
    print('Inicialmente ambos tem 1000 pontos!')
    print('[S] para sair!')
    print(f'[P1] para ver seus pontos {jogador1}')
    print(f'[P2] para ver seus pontos {jogador2}')
    print('[J] para jogar: ')
    while True:
        print('=' * 30)
        opcao = input('Opção: ').upper()
        print('=' * 30)

        while True:
            menu = True
            na = random.choice(dado)
            if na <= 3:
                valor = 'L'
            else:
                valor = 'H'

            if opcao == 'J':
                while True:
                    try:
                        if pontos_jogador1 <=0 or pontos_jogador2 <=0:
                            if pontos_jogador1 <=0 and pontos_jogador2 > 0:
                                print(f'{jogador2} Venceu')
                            if pontos_jogador2 <=0 and pontos_jogador1 > 0:
                                print(f'{jogador1} Venceu')
                            if pontos_jogador1 <= 0 and pontos_jogador2 <= 0:
                                print('Empate')
                            exit()
                            break
                        apostaj1 = int(input(f'Quantos pontos {jogador1}: '))
                        apostaj2 = int(input(f'Quantos pontos {jogador2}: '))
                        if apostaj1 <= 0 or apostaj1 > pontos_jogador1:
                            print(f'{jogador1}O valor deve ser maior que 0, seus pontos são {pontos_jogador1}: ')
                        if apostaj2 <= 0 or apostaj2 > pontos_jogador2:
                            print(f'{jogador2}O valor deve ser maior que 0, seus pontos são {pontos_jogador1}: ')
                        else:
                            low_highj1 = input(f'{jogador1}|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            low_highj2 = input(f'{jogador2}|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            break
                    except ValueError:
                        print('valor inválido, digite apenas números inteiros.')
                
                
                while low_highj1 != 'H' and low_highj1 != 'L' and low_highj1 != 'S':
                    print('Valor inválido')
                    low_highj1 = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                while low_highj2 != 'H' and low_highj2 != 'L' and low_highj2 != 'S':
                    print('Valor inválido')
                    low_highj2 = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                
                if low_highj1 == valor and (low_highj1 == 'L' or low_highj1 == 'H'):
                    print(f'{jogador1} Você acertou e ganhou {apostaj1} pontos!!')
                    pontos_jogador1 = pontos_jogador1 + apostaj1
                    menu = False
                elif low_highj1 == 'L' or low_highj1 == 'H':
                    print(f'{jogador1} Você errou e perdeu {apostaj1} pontos!!')
                    pontos_jogador1 = pontos_jogador1 - apostaj1
                    menu = False

                if low_highj2 == valor and (low_highj2 == 'L' or low_highj2 == 'H'):
                    print(f'{jogador2} Você acertou e ganhou {apostaj2} pontos!!')
                    pontos_jogador2 = pontos_jogador2 + apostaj2
                    menu = False
                elif low_highj2 == 'L' or low_highj2 == 'H':
                    print(f'{jogador2} Você errou e perdeu {apostaj2} pontos!!')
                    pontos_jogador2 = pontos_jogador2 - apostaj2
                    menu = False
                    
                if low_highj1 == 'S' or low_highj2 == 'S':
                    menu = True
                    break
                 
                print()
                print(f'Dado: {na} = {valor}')

                print(f'{jogador1} Seus pontos: {pontos_jogador1}')
                print(f'{jogador2} Seus pontos: {pontos_jogador2}')
                print('=' * 30)

            if opcao == 'S':
                exit()
                pontos_jogador1 = 1000
                pontos_jogador2 = 1000
            if opcao == 'P1':
                print(f'{jogador1} possui {pontos_jogador1} pontos.')
            if opcao == 'P2':
                print(f'{jogador2} possui {pontos_jogador2} pontos.')

            if menu == True:
                print('=' * 30)
                opcao = input('Opção: ').upper()
                print('=' * 30)
