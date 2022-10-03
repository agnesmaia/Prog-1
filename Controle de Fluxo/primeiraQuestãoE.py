from csv import writer

def addNewRegisters(nome, ano, sexo, numero):
    try:
        with open('dados_usuario.csv', 'r', encoding="utf-8") as f:
            ID = len(f.readlines())-1
        list=[ID, ano,sexo,nome,numero]
        with open('dados_usuario.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()

    except FileNotFoundError:
        print('Arquivo não encontrado')


year = input('Digite o ano que deseja adicionar: ')
gender = input('Digite o sexo que deseja adicionar: ')
name = input('Digite o nome que deseja adicionar: ')
number = input('Digite o número que deseja adicionar: ')

addNewRegisters(name, year, gender, number)

