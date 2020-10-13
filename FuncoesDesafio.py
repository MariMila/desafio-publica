def quebras_positivas(pontuacoes):
    """Recebe uma lista com as pontuacoes dos jogos registrados e retorna a
    lista contendo a posição das quebras positivas e a quantidades de vezes
    que houve as quebras e a lista de maximos na ordem em que ocorreram"""
    contador = 0
    maximo = pontuacoes[0]
    lista = []
    maxi = []
    for i in pontuacoes:
        if i > maximo:
            maximo = i
            contador += 1
        maxi.append(maximo)
        lista.append(contador)
    return lista, maxi


def quebras_negativas(pontuacoes):
    """Recebe uma lista com as pontuacoes dos jogos registrados e retorna a
    lista contendo a posição das quebras negativas e a quantidades de vezes
    que houve as quebras e a lista de minimos na ordem em que ocorreram"""
    contador = 0
    minimo = pontuacoes[0]
    lista = []
    mini = []
    for i in pontuacoes:
        if i < minimo:
            minimo = i
            contador += 1
        mini.append(minimo)
        lista.append(contador)
    return lista, mini


def adiciona_jogo(pontuacoes):
    """Recebe a pontuaçao de um novo jogo e adiciona a lista de pontuacoes"""
    entrada = -1
    while not 0 <= entrada < 1000:
        try:
            entrada = int(input("Por favor, adicione a pontuação do jogador no jogo: "))
        except:
            print("Essa entrada não é válida.")
    verificador = False
    while not verificador:
        resposta = input(f'Você deseja adicionar {entrada} à lista de pontuações? [s/n] ')
        resposta = resposta.lower()
        if "s" in resposta:
            pontuacoes.append(entrada)
            verificador = True
        if "n" in resposta:
            verificador = True


def imprime_tabela(pontuacoes):
    """recebe a lista de pontuacoes e imprime a tabela com os resultados"""
    print(" " + "_" * 10 + " " + "_" * 12 + " " + "_" * 15 + " " + "_" * 15 + " " + "_" * 20 + " " + "_" * 20 + " ")
    print("|" + " " * 10 + "|" + " " * 12 + "|" + " " * 15 + "|" + " " * 15 + "|" + " " * 20 + "|" + " " * 20 + "|")
    print("|" + 'Jogo'.center(10) + "|" + 'Placar'.center(12) + "|" + 'Mínimo da'.center(15) + "|" +
          'Máximo da'.center(15) + "|" + 'Quebra recorde'.center(20) + "|" + 'Quebra recorde'.center(20) + "|")
    print("|" + " " * 10 + "|" + " " * 12 + "|" + 'temporada'.center(15) + "|" + 'temporada'.center(15) + "|" +
          'min.'.center(20) + "|" + 'máx.'.center(20) + "|")
    print("|" + "_" * 10 + "|" + "_" * 12 + "|" + "_" * 15 + "|" + "_" * 15 + "|" + "_" * 20 + "|" + "_" * 20 + "|")
    for i in range(len(pontuacoes)):
        print("|" + " " * 10 + "|" + " " * 12 + "|" + " " * 15 + "|" + " " * 15 + "|" + " " * 20 + "|" + " " * 20 + "|")
        print(f'|{numero_impressao(i+1).center(10)}|{numero_impressao(pontuacoes[i]).center(12)}|'
              f'{numero_impressao(quebras_negativas(pontuacoes)[1][i]).center(15)}|'
              f'{numero_impressao(quebras_positivas(pontuacoes)[1][i]).center(15)}|'
              f'{numero_impressao(quebras_negativas(pontuacoes)[0][i]).center(20)}|'
              f'{numero_impressao(quebras_positivas(pontuacoes)[0][i]).center(20)}|')
        print("|" + "_" * 10 + "|" + "_" * 12 + "|" + "_" * 15 + "|" + "_" * 15 + "|" + "_" * 20 + "|" + "_" * 20 + "|")


def numero_impressao(num):
    """recebe um número e transforma em string para impressão"""
    return str(num).center(4)


def imprime_menu():
    """imprime o menu com os comandos para utilização do app"""
    print("\n\nDigite 1 para imprimir a tabela comparativa dos resultados registrado até o momento\n"
          "Digite 2 para adicionar um novo jogo ao sistema\n"
          "Digite 3 para somente imprimir a pontuação máxima obtida na temporada\n"
          "Digite 4 para somente imprimir a pontuação mínima obtida na temporada\n"
          "Digite 5 para somente imprimir a quantidade de vezes que a pontuação máxima fora quebrada na temporada\n"
          "Digite 6 para somente imprimir a quantidade de vezes que a pontuação mínima fora quebrada na temporada\n"
          "Digite 7 para remover um jovo pré-existente no sistema\n"
          "Digite 8 para remover todos os jogos existentes no sistema\n"
          "Digite 0 para fechar o aplicativo")


def para_salvar(pontuacoes):
    """recebe a lista de pontuações e retorna uma string para que seja salvo para uso posterior"""
    return "pontuacoes = " + str(pontuacoes)


def remove_jogo(pontuacoes):
    """recebe a lista de pontuações e retira o jogo desejado"""
    verifica = True
    cont = 0
    while verifica:
        entrada = input("Digite o número do jogo que você deseja remover do baco de dados: ")
        try:
            entrada = int(entrada)
            verifica = False
            if entrada < 0 or entrada > len(pontuacoes):
                print("Entrada inválida")
                cont += 1
                verifica = True
                if len(pontuacoes) == 0:
                    print("Não há jogos registrados no banco de dados")
                    verifica = False
            else:
                entrada -= 1
                pontuacoes.pop(entrada)
        except:
            print("Entrada inválida")
            cont += 1
        if cont == 3:
            print("Você voltará para o menu anterior")
            verifica = False


def apaga_dados(pontuacoes):
    """recebe a lista com as pontuações e a limpa"""
    entrada = input("Digite 'sim' se você tem certeza que deseja apagar todos os jogos registrados: ")
    entrada = entrada.lower()
    if 's' in entrada:
        pontuacoes.clear()
    else:
        print("Comando cancelado")
