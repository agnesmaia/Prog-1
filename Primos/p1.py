import random
import os

# a

def ePrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False;
    return num > 1;


def osDoisSaoPrimos(n1, n2):
    numbers = [];

    n1Primo = ePrimo(n1);
    n2Primo = ePrimo(n2);

    return n1Primo and n2Primo


resultado = osDoisSaoPrimos(10, 7);

print(resultado);

# B

analise = [];

os.remove("./primos.txt")
arquivo = open("./primos.txt", "a")

for i in range(0, 1000): 
    n1 = random.randint(1, 100);
    n2 = random.randint(1, 100);

    saoPrimos = osDoisSaoPrimos(n1, n2);


    arquivo.write(str(n1) + ", " + str(n2) +  ", " + str(saoPrimos) + "\n");
    analise.append([n1, n2, saoPrimos]);


primos = len(list(filter(lambda item: item[2], analise)));
calc = primos / 10;

print(str(calc) + "%");

