import csv

def nameOccurrence(nome = ''):
    '''
    Número de ocorrências do parâmetro "nome" e Lista de Nomes que iniciam com o valor do parâmentro.

    Arguments:
        nome: uma string

    Returns:
        Quantidade de ocorrências
        
        Lista de Nomes
    '''
    try:
        arquivo = open("dados_usuario.csv")
        linhas = csv.reader(arquivo)
        nameOccurrenceList = []

        for linha in linhas:
            if nome in linha[3]:
                nameOccurrenceList.append(linha[3])
    
        print('Número de Ocorrências: ', len(nameOccurrenceList))
        print(nameOccurrenceList)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception:
        print('Erro em tempo de execução desconhecido')

    
name = input('Digite o nome que você deseja procurar: ')
nameOccurrence(name)



