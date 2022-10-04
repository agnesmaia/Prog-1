import csv

def argOccurrence(arg):
    '''
  Verifica o número de registros que contém a substring arg em uma string de alguma de suas informações

  Arguments:
    arg: uma string

  Returns:
    Lista com os registros encontrados que possuem a substring
  '''
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


