import os

restaurants = ['Pizza', 'Comet']

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

def close_app():
    os.system('clear')
    print('Encerrando o programa')

def return_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def invalid_option():
    print('Opção inválida! \n')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def create_restaurant():
    os.system('clear')
    print('Cadastrar restaurante: \n')
    restaurant_name = input('Digite o nome do restaurante para que deseja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'Restaurante cadastrado com sucesso! \n [ {restaurant_name} ] ✅')

    return_main_menu()

def list_restaurants():
    os.system('clear')
    print('Restaurantes cadastrados: \n')

    for restaurant in restaurants: 
        print(f'- {restaurant} \n')
   
    return_main_menu()

def select_options():
    try:
        option_Choice = int(input('Escolha uma opção: '))
        if option_Choice == 1:
            create_restaurant()
        elif option_Choice == 2:
            list_restaurants()
        elif option_Choice == 3:
            print('Ativar restaurante')
        elif option_Choice == 4:
            close_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    show_program_name()
    show_options()
    select_options()

if __name__ == '__main__':
    main()