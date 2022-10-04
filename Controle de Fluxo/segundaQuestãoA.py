def chainOccurrence(cadeia, padrao):
  '''
  Informa a quantidade de vezes que o valor 'padrao' aparece em 'cadeia'

  Arguments:
    cadeia: uma string
    padrao: uma string

  Returns:
    Retorna o Número de registros de 'padrao' encontrados em 'cadeia'
  '''
  try:
    numberOfOccurrences = cadeia.count(padrao)
    print(numberOfOccurrences)
  except Exception:
    print('Tempo em erro de execução desconhecido.')

cadeia = input("Digite a Cadeia de caracteres: ")
padrao = input("Digite o padrão que deseja encontrar: ")

chainOccurrence(cadeia, padrao)