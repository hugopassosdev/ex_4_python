nome = input("Insira seu nome completo: ")

execute = True

while(execute == True):
    ano_nascimento = int(input('Insira o ano o qual nasceu: '))
    try:
        if(ano_nascimento < 1922) or (ano_nascimento > 2021):
            print('Favor digitar um ano entre 1922 e 2021!')
            continue
        else:
            idade = 2022 - ano_nascimento
            print(f'{nome} possui {idade} anos em 2022!')
            break 
    except:
        print('O ano deve ser um número inteiro.')