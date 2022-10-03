import csv

def argOccurrence(arg):
    try:
        arquivo = open("dados_usuario.csv")
        linhas = csv.reader(arquivo)
        argOccurrenceList = []

        for linha in linhas:
            if arg in linha:
                x = linha.index(arg)
                argOccurrenceList.append(linha[x])
    
        print(argOccurrenceList)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception:
        print('Erro em tempo de execução desconhecido')

    
argument = input('Digite o que você deseja procurar: ')
argOccurrence(argument)


