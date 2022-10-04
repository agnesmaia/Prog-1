def maxFrequency():
  '''
  Analisa os registros e informa a frequência máxima do padrão 'ATGCCA'

  Returns:
    Retorna a frequência máxima dos registros
  '''
  try:
    maxFrequency = 0
    with open('colunas.txt', 'r', encoding= 'utf-8') as f:
      for linha in f.readlines()[1:]:
        column = linha.split(sep=',')
        if int(column[1]) > maxFrequency:
          maxFrequency = int(column[1])
    return maxFrequency
  except ValueError:
    print('Código inválido: valor deve ser númerico')
  except Exception:
    print('Erro em tempo de execução desconhecido')

def maxFrequencyLines():
  '''
  Analisa os registros e informar em qual/quais linhas estão as frequências máximas

  Returns:
    Retorna uma lista com os índices das linhas
  '''
  try:
    index = []
    contador = 2 
    maxFrequencyRegister = maxFrequency()
    with open('colunas.txt', 'r', encoding= 'utf-8') as f:
      for linha in f.readlines()[1:]: 
        linha_separada = linha.split(sep=',')
        if int(linha_separada[1]) == maxFrequencyRegister:
          index.append(contador)
        contador += 1
    print(index)
  except Exception:
    print('Erro em tempo de execução desconhecido')




print(maxFrequency())
maxFrequencyLines()
