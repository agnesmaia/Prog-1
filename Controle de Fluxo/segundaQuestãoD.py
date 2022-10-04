def notChainRegisters():
  '''
  Conta o número de sequências que não possui o padrão "ATGCCA"

  Returns:
    Retorna o número de sequências
  ''' 
  try:
    count = 0
    with open('colunas.txt', 'r', encoding= 'utf-8') as f:
        for linha in f:
            column = linha.split(sep=',')
            if column[0] == 'False':
                count += 1
    print(count)
  except Exception:
    print('Erro em tempo de execução desconhecido')
 
notChainRegisters()