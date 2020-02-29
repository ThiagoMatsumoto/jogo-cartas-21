import time
import random
import sys
import os

baralho_original = {

    'As Copas': 11, 'As Paus': 11, 'As Espada': 11, 'As Ouros': 11,
    '2 Copas': 2, '2 Paus': 2, '2 Espada': 2, '2 Ouros': 2,
    '3 Copas': 3, '3 Paus': 3, '3 Espada': 3, '3 Ouros': 3,
    '4 Copas': 4, '4 Paus': 4, '4 Espada': 4, '4 Ouros': 4,
    '5 Copas': 5, '5 Paus': 5, '5 Espada': 5, '5 Ouros': 5,
    '6 Copas': 6, '6 Paus': 6, '6 Espada': 6, '6 Ouros': 6,
    '7 Copas': 7, '7 Paus': 7, '7 Espada': 7, '7 Ouros': 7,
    '8 Copas': 8, '8 Paus': 8, '8 Espada': 8, '8 Ouros': 8,
    '9 Copas': 9, '9 Paus': 9, '9 Espada': 9, '9 Ouros': 9,
    '10 Copas': 10, '10 Paus': 10, '10 Espada': 10, '10 Ouros': 10,
    'J Copas': 10, 'J Paus': 10, 'J Espada': 10, 'J Ouros': 10,
    'Q Copas': 10, 'Q Paus': 10, 'Q Espada': 10, 'Q Ouros': 10,
    'K Copas': 10, 'K Paus': 10, 'K Espada': 10, 'K Ouros': 10

}
# cópia p/ manipular a escolha de cartas sem afetar o calculo da pontuação
baralho_copia = dict(baralho_original)

# cartas para conferir o blackjack
cartas_as = [

    'As Copas', 'As Paus', 'As Espada', 'As Ouros'

]
cartas_10 = [

    '10 Copas', '10 Paus', '10 Espada', '10 Ouros',
    'J Copas', 'J Paus', 'J Espada', 'J Ouros',
    'Q Copas', 'Q Paus', 'Q Espada', 'Q Ouros',
    'K Copas', 'K Paus', 'K Espada', 'K Ouros'

]

def gerador_de_cartas():
    cartas = list(baralho_copia)
    carta_aleatoria = random.choice(cartas)
    del baralho_copia[carta_aleatoria] #remover a cópia para não repetir
    return carta_aleatoria

def conferir_blackjack(lista):
    if (lista[0] in cartas_as and lista[1] in cartas_10):
        blackjack = True
        print('Blackjack!')
    elif (lista[1] in cartas_as and lista[0] in cartas_10):
        blackjack = True
        print('Blackjack!')
    else:
        blackjack = False
    return blackjack

def vitoria_blackjack(bool1, bool2):
    if (bool1 == False and bool2 == False):
        return False
    if (bool1 == bool2):
        print('Empate!')
        return True
    elif(bool1 == True):
        print('Você ganhou!')
        return True
    elif (bool2 == True):
        print('A mesa ganhou!')
        return True

def verificar_as(lista):
    for i in lista:
        if(i == 'As Copas' or i == 'As Paus' or i == 'As Espada' or i == 'As Ouros'):
            valor_as = int(input('Qual valor do As deseja utilizar? [1 ou 11]\n'))
            if valor_as == 1:
                baralho_original[i] = 1
            elif valor_as == 11:
                baralho_original[i] = 11

def pontuacao_cartas(lista, dict):
    for a, b in baralho_original.items():
        for i in lista:
            if (i == a):
                dict[a] = b
    return sum(dict.values())

def comprar_mais(cartasLista):
    cartasLista.append(gerador_de_cartas())
    return cartasLista

def jogar_novamente():
    """Não salva o progresso, precisa ser feito
    antes da chamada da função"""
    python = sys.executable
    os.execl(python, python, * sys.argv)


print("Jogo de cartas: 21\n")

time.sleep(1)

print('Suas cartas:')
carta1_jogador = gerador_de_cartas()
carta2_jogador = gerador_de_cartas()
print(carta1_jogador + ' | ' + carta2_jogador + '\n')
cartas_jogador = [carta1_jogador, carta2_jogador]
jogador_dict_pontos = {}


time.sleep(1.5)

print('Cartas da mesa:')
carta1_mesa = gerador_de_cartas()
carta2_mesa = gerador_de_cartas()
print(carta1_mesa + ' | ' + 'Carta escondida' + '\n')
cartas_mesa = [carta1_mesa, carta2_mesa]
mesa_pontos = {}


#armazenar se teve ou não blackjack [true ou false]
blackjack_jogador = bool(conferir_blackjack(cartas_jogador))
blackjack_mesa = bool(conferir_blackjack(cartas_mesa))

if blackjack_jogador == True:
    print('Jogador tem blackjack')
if blackjack_mesa == True:
    print('Mesa tem blackjack')

#com true ou false, verificar se foi vitoria, empate ou derrota e finalizar o jogo
vitoria = bool(vitoria_blackjack(blackjack_jogador, blackjack_mesa))
if (vitoria == True):
    sys.exit('Fim de jogo!')

time.sleep(1)

#caso a condição acima não ocorra, continuar para verificar se o jogador tem As
#e ele decidir qual valor quer usar
verificar_as(cartas_jogador)

for i in cartas_mesa:
    if(i == 'As Copas' or i == 'As Paus' or i == 'As Espada' or i == 'As Ouros'):
        if pontuacao_cartas(cartas_mesa, mesa_pontos) > 21 :
            valor_as = 1
        else:
            valor_as = 11
        if valor_as == 1:
            baralho_original[i] = 1
        elif valor_as == 11:
            baralho_original[i] = 11

time.sleep(1.5)

#comprar mais cartas para o jogador
mais_cartas = input("Quer comprar mais cartas? (S ou N) \n")

time.sleep(1)

while mais_cartas == 'S':
    cartas = comprar_mais(cartas_jogador)
    verificar_as(cartas_jogador)
    print(' | '.join(cartas))
    pontos_total_jogador = pontuacao_cartas(cartas_jogador, jogador_dict_pontos)
    print(pontos_total_jogador)
    if(pontos_total_jogador == 21):
        print('\n 21! Espere a mesa jogar')
        break
    if(pontos_total_jogador > 21):
        print('\n Você perdeu!')
        break
    time.sleep(1)
    mais_cartas = input("Quer comprar mais cartas? (S ou N) \n")


total_final_jogador = pontuacao_cartas(cartas_jogador, jogador_dict_pontos)
total_final_mesa = pontuacao_cartas(cartas_mesa, mesa_pontos)

while (total_final_mesa < total_final_jogador and total_final_jogador <= 21):
    cartas_novas_mesa = comprar_mais(cartas_mesa)
    total_final_mesa = pontuacao_cartas(cartas_mesa, mesa_pontos)
    if(total_final_jogador - total_final_mesa <= 2):
        break
    if(total_final_mesa > 21):
        print('\n' + "A mesa passou de 21! Jogador vence!")

time.sleep(1.5)
print('\nSua mão: ' + ' | '.join(cartas_jogador))
print('Total: ' + str(total_final_jogador) + '\n')
print('Mesa: ' + ' | '.join(cartas_mesa))
print('Total: ' + str(total_final_mesa) + '\n')

if(total_final_jogador < total_final_mesa and total_final_mesa <= 21):
    print('A mesa tem a mão mais alta!\n')
elif(total_final_jogador > total_final_mesa and total_final_jogador <= 21):
    print('Parabéns! Sua mão é a mais alta do que a mesa\n')
elif(total_final_jogador == total_final_mesa):
    print('Empate!')

if __name__ == "__main__":
    resposta = str(input("Quer jogar novamente? "))
    if resposta.lower().strip() in "S s Sim sim".split():
        jogar_novamente()
