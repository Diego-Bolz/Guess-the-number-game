# Módulo de jogo de adivinhação

# O algoritmo pede ao usuário para selecionar uma dificuldade
# Fácil (1-10), Médio (1-50) ou Difícil(1-100)
# O algoritmo gera um número aleatório baseado na dificuldade e então pede chutes ao usuário (que serão guardados na lista "erros")
# Se o usuário chutar 5 vezes sem ter acertado nenhum chute aparece uma mensagem de derrota
# Caso ele acerte o chute em qualquer vez aparece uma mensagem de vítoria e o número de chutes
# E então no final de ambas as mensagens o algoritmo mostra os números chutados através da lista "erros"
import random
erros = []
chute = 0
tentativas = 0
divisor = '------------------------------'
dificuldade = int(input('\tEscolha um nível de dificuldade!\n[1] Fácil (1-10)\n[2] Médio (1-50)\n[3] Difícil (1-100)\n'))
if dificuldade == 1:
     numero_aleatorio = random.randint(1,10)
elif dificuldade == 2:
     numero_aleatorio = random.randint(1,50)
elif dificuldade == 3:
    numero_aleatorio = random.randint(1, 100)
while chute != numero_aleatorio and tentativas < 5:
    chute = int(input(f'{divisor}\nChute um número: '))
    erros.append(chute)
    tentativas += 1
    if chute > numero_aleatorio:
        print(f'Muito alto!')
    elif chute < numero_aleatorio:
        print(f'Muito baixo!')
if chute == numero_aleatorio:
    print(f'{divisor}\nAcertou! o número era {numero_aleatorio}!')
    print(f'Você chutou {tentativas} vezes')
else:
    print(f'{divisor}\nAcabou suas tentativas! :(')
print(f'Números chutados: {erros}')