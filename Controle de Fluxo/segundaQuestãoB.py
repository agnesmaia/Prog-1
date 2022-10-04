def chainOccurrence(cadeia, padrao):
  '''
  Informa se 'padrao' está contido em 'cadeia'

  Arguments:
    cadeia: uma string
    padrao: uma string
  Returns:
    True:   'padrao' contido em 'cadeia'
    False:  'padrao' não contido em 'cadeia'
  '''
  try:
    if padrao in cadeia:
      print(True) 
    else:
      print(False)
  except Exception:
    print('Tempo em erro de execução desconhecido.')

cadeia = input("Digite a Cadeia de caracteres: ")
padrao = input("Digite o padrão que deseja encontrar: ")

chainOccurrence(cadeia, padrao)