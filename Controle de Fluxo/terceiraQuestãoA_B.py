import random
import os

# A

def ePrimo(num):
    """
        Informa se o número é primo
    Args:
        num: número inteiro
    Returns:
        False: se o número não for primo
        True: se o número for primo
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1


def osDoisSaoPrimos(n1, n2):
    """Analisa se n1 e n2 são primos entre si

    Args:
        n1: número inteiro
        n2: número inteiro

    Returns:
        True: se os dois números forem primos
        False: se pelo menos um deles não for primo
    """
    numbers = []

    n1Primo = ePrimo(n1)
    n2Primo = ePrimo(n2)

    return n1Primo and n2Primo

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = osDoisSaoPrimos(num1, num2)

print(resultado)

# B

analise = [];

os.remove("./primos.txt")
arquivo = open("./primos.txt", "a")

for i in range(0, 1000): 
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)

    saoPrimos = osDoisSaoPrimos(n1, n2)


    arquivo.write(str(n1) + ", " + str(n2) +  ", " + str(saoPrimos) + "\n")
    analise.append([n1, n2, saoPrimos])


primos = len(list(filter(lambda item: item[2], analise)))
calc = primos / 10

print(str(calc) + "%")