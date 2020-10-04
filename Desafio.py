import FuncoesDesafio as fdd
import salvos as save
pontuacoes = save.pontuacoes


def main():
    print("Seja bem-vindo(a)! \nEsse é aplicativo que visa auxiliá-lo(a) no controle de seus resultados")
    fdd.imprime_menu()
    entrada = input("Digite sua escolha (0-8): ")
    while entrada != 0:
        try:
            entrada = int(entrada)
        except:
            entrada = 10
        if entrada == 1:
            fdd.imprime_tabela(pontuacoes)
        elif entrada == 2:
            fdd.adiciona_jogo(pontuacoes)
        elif entrada == 3:
            print(f'A pontuação máxima obtida na temporada foi {max(pontuacoes)}')
        elif entrada == 4:
            print(f'A pontuação mínima obtida na temporada foi {min(pontuacoes)}')
        elif entrada == 5:
            print(f'O recorde de pontuação máxima foi quebrado {fdd.quebras_positivas(pontuacoes)[0][-1]} vezes na temporada')
        elif entrada == 6:
            print(f'O recorde de pontuação mínima foi quebrado {fdd.quebras_negativas(pontuacoes)[0][-1]} vezes na temporada')
        elif entrada == 7:
            fdd.remove_jogo(pontuacoes)
        elif entrada == 8:
            fdd.apaga_dados(pontuacoes)
        elif entrada == 9:
            fdd.imprime_menu()
        if entrada != 0:
            if entrada != 9:
                print("\n\nAcaso queira que o menu seja impresso novamente Digite 9\n")
            entrada = input("Digite sua escolha (0-9): ")
        if entrada == 0:
            salva = input('Se você deseja salvar os jogos inseridos até aqui, por favor digite "Sim": ')
            if 's' in salva:
                with open('salvos.py', 'w') as arquivo:
                    arquivo.write(fdd.para_salvar(pontuacoes))
                    arquivo.close()


main()