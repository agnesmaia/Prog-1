import csv

def yearOrGenderOccurrence(ano, sexo):
    try:
        arquivo = open("dados_usuario.csv")
        linhas = csv.reader(arquivo)
        yearOccurrenceList = []
        genderOccurrenceList = []

        for linha in linhas:
            if ano == linha[1]:
                yearOccurrenceList.append(linha[1])
            if sexo in linha[2]:
                genderOccurrenceList.append(linha[2])
            

        print('Número de Ocorrências do Ano: ', len(yearOccurrenceList))
        print('Número de Ocorrências do Sexo: ', len(genderOccurrenceList))

    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception:
        print('Erro em tempo de execução desconhecido')
    
year = input('Digite o ano que você deseja procurar: ')
gender = input('Digite F para Feminino e M para Masculino: ')

yearOrGenderOccurrence(year, gender)

