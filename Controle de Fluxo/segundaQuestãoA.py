def chainOccurrence(cadeia, padrao):
  '''
  Informa a quantidade de vezes que o valor 'padrao' aparece em 'cadeia'

  Arguments:
    padrao: uma string
    cadeia: uma string

  Returns:
    Retorna o Número de registros de 'padrao' encontrados em 'cadeia'
  '''
  try:
    numberOfOccurrences = cadeia.count(padrao)
    print(numberOfOccurrences)
  except Exception:
    print('Tempo em erro de execução desconhecido.')

chainOccurrence(
    input('Cadeia: '),
    input('Padrão: ') 
)