import os

def show_program_name():
    print("""
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃╱┃╭━╮┃
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮╭╮╭╋╮┃╱┃┃┃┃┃
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫┃╰╯┃┃┃╱┃┃┃┃┃
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃╰╮╭╋╯╰┳┫╰━╯┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯╱╰┻┻━━┻┻━━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯ \n""" )

def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def invalid_option():
    print('Opção inválida! \n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def select_options():
    try:
        option_Choice = int(input('Escolha uma opção: '))
        if option_Choice == 1:
            print('Cadastrar restaurante')
        elif option_Choice == 2:
            print('2. Listar restaurante')
        elif option_Choice == 3:
            print('Ativar restaurante')
        elif option_Choice == 4:
            close_app()
        else:
            invalid_option()
    except:
        invalid_option()

def close_app():
    os.system('clear')
    print('Encerrando o programa')

def main():
    os.system('clear')
    show_program_name()
    show_options()
    select_options()

if __name__ == '__main__':
    main()