import csv

def numberOccurrence(numero):
    try:
        arquivo = open("dados_usuario.csv")
        linhas = csv.reader(arquivo)
        IdsOccurrenceList = []

        for linha in linhas:
            if numero in linha:
                IdsOccurrenceList.append(linha[0])
    
        print(IdsOccurrenceList)
        
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception:
        print('Erro em tempo de execução desconhecido')

    
number = input('Digite o número que você deseja achar: ')
numberOccurrence(number)

