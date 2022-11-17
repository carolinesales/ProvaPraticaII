import random

jogar = 1
vitoria = 1


#criar uma lista chamada dado com os valores [1,2,3,4,5,6] referentes aos lados de dado comum
dado = [1, 2, 3, 4, 5, 6]

#Em seguida, crie duas listas vazias chamadas Player1 e Player 2.

player1 = []
player2 = []

#A partir disso, você deve criar um menu com as opções 1 - começar e 2 - encerrar

opcao = int(input("selecione a opção desejada: \n 1) começar \n 2)Encerrar"))

#Quando a opção 1 for escolhida, o programa deve randomizar um valor da lista dado e armazenar na lista dos jogadores de
#forma intercalada

if opcao == 1:
    while jogar == 1:

        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)

        if player1 == player2:
            print("Empate")

            break



#o usuario pode jogar quantas vezes quiser e cada jogada realizada o programa deve exibir qual é o jogador da vez e qual
#número esse jogador tirou no dado

#quando o usuario informar a opção 2(encerrar) o prgrama deve exibir todos os valores tirados de cada jogador
if opcao == 2:
    print("O player", vitoria, "foi o vencedor")
    print("Obrigado por Jogar")


#a soma dos valores de cada jogador
# e qual o vencedor



