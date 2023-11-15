execute = True

while(execute == True):
    nome = input("Insira seu nome completo: ")
    ano_nascimento = int(input("Insira o ano o qual nasceu: "))
    try:
        if(ano_nascimento >= 1922) and (ano_nascimento <= 2021):
            idade = 2022 - ano_nascimento
            print(f'{nome} possui {idade} anos!') 
        else:
            print('Você digitou uma data de nascimento inválida!')
    except:
        print('Favor digitar um caractere, favor digitar uma data.')