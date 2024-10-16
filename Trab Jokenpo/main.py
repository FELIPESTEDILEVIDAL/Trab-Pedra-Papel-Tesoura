from random import choice #importa a função choice do múdulo random

acoes_permitidas = ['pedra', 'papel', 'tesoura'] #lista com as ações utilizadas
ponto_AI_1 = 0 #contador de ponto do PC
ponto_Usuario = 0 #contador de ponto do Usuário
cont = 0 #contador do while


amarelo = '\033[33m' #estilização das strings
original = '\033[0;0m' 
negrito = '\033[1m'

def ponto_ai_1(): #função resposável por adicionar pontos para a IA
    global ponto_AI_1 #pega a variavel criada no início do código
    print(amarelo + 'Ponto da AI 1\n'+ original) #imprime o resultado, caso a IA faça ponto
    ponto_AI_1 += 1 #adiciona ponto

def ponto_usuario(): #função resposável por adicionar pontos para o Usuario
    global ponto_Usuario #pega a variavel criada no início do código
    print(amarelo + 'Ponto do Usuario\n'+ original)  #imprime o resultado, caso o Usuario faça ponto
    ponto_Usuario += 1 #adiciona ponto

while cont < 3: #cria um loop que vai rodar 3 vezes 
    movimento_AI_1 = str(choice(acoes_permitidas)) #utiliza a função choice dentro da variavel acoes permitidas
    movimento_Usuario = input('Escolha qual opcao (pedra, papel, tesoura): ') #pede para o usuario escolher uma jogada
    movimento_Usuario.lower() #evita erros de letra maiuscula, transformando a str toda em letra minuscula
    while movimento_Usuario not in acoes_permitidas: #cria um loop, caso o usuario escreva sua jogada errado
        movimento_Usuario = input('Escolha qual opcao (pedra, papel, tesoura): ') #pede para o usuario escolher uma jogada
        movimento_Usuario.lower() #evita erros de letra maiuscula, transformando a str toda em letra minuscula
        
    print(f'AI 1 escolheu {movimento_AI_1}\nUsuario escolheu {movimento_Usuario}') #Imprime a jogada dos jogadores
    if movimento_AI_1 == movimento_Usuario: #compara para ver se as jogadas são iguais
        print(amarelo + 'Empatou\n' + original) #imprime que o resultado é empate

    elif movimento_AI_1 == 'pedra' and movimento_Usuario == 'tesoura': 
        ponto_ai_1() #chama a funçao que acrescenta ponto para a IA
    elif movimento_AI_1 == 'tesoura' and movimento_Usuario == 'papel': #compara todas as jogadas possiveis para a IA fazer ponto
        ponto_ai_1() #chama a funçao que acrescenta ponto para a IA
    elif movimento_AI_1 == 'papel' and movimento_Usuario == 'pedra':
        ponto_ai_1() #chama a funçao que acrescenta ponto para a IA
    
    elif movimento_Usuario == 'pedra' and movimento_AI_1 == 'tesoura':
        ponto_usuario() #chama a funçao que acrescenta ponto para o Usuario
    elif movimento_Usuario == 'tesoura' and movimento_AI_1 == 'papel': #compara todas as jogadas possiveis para o Ususario fazer ponto
        ponto_usuario() #chama a funçao que acrescenta ponto para o Usuario
    elif movimento_Usuario == 'papel' and movimento_AI_1 == 'pedra':
        ponto_usuario() #chama a funçao que acrescenta ponto para o Usuario
    cont += 1

print(negrito + amarelo + 'Pontuacao final' + original) #imprime a pontuação final
print(f'AI 1 fez {ponto_AI_1}\nUsuario fez {ponto_Usuario}') #imprime a quantidade de pontos de cada jogador