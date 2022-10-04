

def numberOfChainOccurrence(cadeia, padrao):
 
  try:
    numberOfOccurrences = cadeia.count(padrao)
    return numberOfOccurrences
  except Exception:
    print('Tempo em erro de execução desconhecido.')


def chainOccurrence(cadeia, padrao):

  try:
    if padrao in cadeia:
      return True
    else:
      return False
  except Exception:
    print('Tempo em erro de execução desconhecido.')


def chainRegisters():
  '''
  Gera um novo arquivo de texto, construindo uma tabela nesse arquivo informando se ocorreu o padrão na cadeia e quantas vezes ele ocorreu.
  '''
  try:
    with open('colunas.txt', 'a', encoding= 'utf-8') as f:
      f.write('TEM_ATGCCA,FREQ_ATGCCA')
    with open('dados_DNA.txt', 'r', encoding= 'utf-8') as f:
      for linha in f:
        registers = chainOccurrence(linha, 'ATGCCA')
        numberOfRegisters = numberOfChainOccurrence(linha,'ATGCCA')
        with open('colunas.txt', 'a', encoding= 'utf-8') as f:
          f.write('\n')
          f.write(f'{registers},{numberOfRegisters}')
  except FileNotFoundError:
    with open('colunas.txt','x', encoding= 'utf-8') as f:
      f.write('TEM_ATGCCA,FREQ_ATGCCA')
  except Exception:
    print('Tempo em erro de execução desconhecido.')
    
chainRegisters()