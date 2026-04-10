import os

restaurants = []

def show_program_name():
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃╱┃╭━╮┃
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮╭╮┣╮┃╱┃┃┃┃┃
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫┃╰╯┃┃╱┃┃┃┃┃
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃╰╮╭╯╰┳┫╰━╯┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯╱╰┻━━┻┻━━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯\n""" )

def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def close_app():
    show_subtitle('Encerrando o programa')

def return_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def invalid_option():
    print('Opção inválida! \n')

    return_main_menu()

def show_subtitle(text):
    os.system('clear')
    print(text)
    print()

def create_restaurant():
    show_subtitle('Cadastrar restaurante: ')
    restaurant_name = input('Digite o nome do restaurante para que deseja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'Restaurante cadastrado com sucesso! \n [ {restaurant_name} ] ✅')

    return_main_menu()

def list_restaurants():
    show_subtitle('Restaurantes cadastrados: ')

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