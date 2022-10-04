import csv

def yearOrGenderOccurrence(ano, sexo):
    '''
  Número de registros com year maior ou igual ao valor do parâmetro ano e gender igual ao valor do parâmetro sexo. 

  Arguments:
    ano:  um número inteiro
    sexo: uma string. Valores Possíveis: 'M' 'F'

  Returns:
    Número de Ocorrências de Ano
    Número de Ocorrências de Sexo
  '''
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

