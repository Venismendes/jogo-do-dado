import random

player1_points = 1000
player2_points = 1000
dado = (1, 2, 3, 4, 5, 6)
players = 1

player = input('Olá qual o seu nome: ')
print(f'Bem vindo ao jogo do dado {player}')


quantidade_jogadores = input('Deseja jogador de 2 jogadores? [S/N]: ').upper()


if quantidade_jogadores == 'S':
    players = 2
    player1 = player
    player2 = input('Nome do segundo jogador: ')


print('=' * 40)
while players == 1:
    print('Inicialmente você tem 1000 pontos!')
    print('[S] para sair!')
    print('[P] para ver seus pontos')
    print('[J] para jogar: ')
    while True:
        print('=' * 30)
        option = input('Opção: ').upper()
        print('=' * 30)

        while True:
            menu = True
            dice = random.choice(dado)
            if dice <= 3:
                value = 'L'
            else:
                value = 'H'

            if option == 'J':
                while True:
                    try:
                        if player1_points <= 0:
                            print('Fim do jogo!!')
                            exit()
                        bet = int(input('Quantos pontos: '))
                        if bet <= 0 or bet > player1_points:
                            print(f'O valor deve ser maior que 0, seus pontos são {player1_points}: ')

                        else:
                            low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            break
                    except ValueError:
                        print('valor inválido, digite apenas números inteiros.')
                
                
                while low_high != 'H' and low_high != 'L' and low_high != 'S':
                    print('Valor inválido')
                    low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                
                if low_high == value and (low_high == 'L' or low_high == 'H'):
                    print(f'Você acertou e ganhou {bet} pontos!!')
                    player1_points = player1_points + bet
                    menu = False
                elif low_high == 'L' or low_high == 'H':
                    print(f'Você errou e perdeu {bet} pontos!!')
                    player1_points = player1_points - bet
                    menu = False
                    
                if low_high == 'S':
                    menu = True
                    break
                 
                print()
                print(f'Dado: {dice} = {value}')

                print(f'Seus pontos: {player1_points}')
                print('=' * 30)

            if option == 'S':
                exit()
            if option == 'P':
                print(f'Você possui {player1_points} pontos.')

            if menu == True:
                print('=' * 30)
                option = input('Opção: ').upper()
                print('=' * 30)
print('=' * 40)
while players == 2:
    print('Inicialmente ambos tem 1000 pontos!')
    print('[S] para sair!')
    print(f'[P1] para ver seus pontos {player1}')
    print(f'[P2] para ver seus pontos {player2}')
    print('[J] para jogar: ')
    while True:
        print('=' * 30)
        option = input('Opção: ').upper()
        print('=' * 30)

        while True:
            menu = True
            dice = random.choice(dado)
            if dice <= 3:
                value = 'L'
            else:
                value = 'H'

            if option == 'J':
                while True:
                    try:
                        if player1_points <=0 or player2_points <=0:
                            if player1_points <=0 and player2_points > 0:
                                print(f'{player2} Venceu')
                            if player2_points <=0 and player1_points > 0:
                                print(f'{player1} Venceu')
                            if player1_points <= 0 and player2_points <= 0:
                                print('Empate')
                            exit()
                            break
                        apostaj1 = int(input(f'Quantos pontos {player1}: '))
                        apostaj2 = int(input(f'Quantos pontos {player2}: '))
                        if apostaj1 <= 0 or apostaj1 > player1_points:
                            print(f'{player1}O valor deve ser maior que 0, seus pontos são {player1_points}: ')
                        if apostaj2 <= 0 or apostaj2 > player2_points:
                            print(f'{player2}O valor deve ser maior que 0, seus pontos são {player1_points}: ')
                        else:
                            low_highj1 = input(f'{player1}|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            low_highj2 = input(f'{player2}|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                            break
                    except ValueError:
                        print('valor inválido, digite apenas números inteiros.')
                
                
                while low_highj1 != 'H' and low_highj1 != 'L' and low_highj1 != 'S':
                    print('Valor inválido')
                    low_highj1 = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                while low_highj2 != 'H' and low_highj2 != 'L' and low_highj2 != 'S':
                    print('Valor inválido')
                    low_highj2 = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                
                if low_highj1 == value and (low_highj1 == 'L' or low_highj1 == 'H'):
                    print(f'{player1} Você acertou e ganhou {apostaj1} pontos!!')
                    player1_points = player1_points + apostaj1
                    menu = False
                elif low_highj1 == 'L' or low_highj1 == 'H':
                    print(f'{player1} Você errou e perdeu {apostaj1} pontos!!')
                    player1_points = player1_points - apostaj1
                    menu = False

                if low_highj2 == value and (low_highj2 == 'L' or low_highj2 == 'H'):
                    print(f'{player2} Você acertou e ganhou {apostaj2} pontos!!')
                    player2_points = player2_points + apostaj2
                    menu = False
                elif low_highj2 == 'L' or low_highj2 == 'H':
                    print(f'{player2} Você errou e perdeu {apostaj2} pontos!!')
                    player2_points = player2_points - apostaj2
                    menu = False
                    
                if low_highj1 == 'S' or low_highj2 == 'S':
                    menu = True
                    break
                 
                print()
                print(f'Dado: {dice} = {value}')

                print(f'{player1} Seus pontos: {player1_points}')
                print(f'{player2} Seus pontos: {player2_points}')
                print('=' * 30)

            if option == 'S':
                exit()
                player1_points = 1000
                player2_points = 1000
            if option == 'P1':
                print(f'{player1} possui {player1_points} pontos.')
            if option == 'P2':
                print(f'{player2} possui {player2_points} pontos.')

            if menu == True:
                print('=' * 30)
                option = input('Opção: ').upper()
                print('=' * 30)
