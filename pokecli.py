import pokebase as pb
from colorama import Fore, Style
from art import text2art
from term_image.image import *
import os

# Colores

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def buscar_pokemon():
    
    input_pokemon = (input(f'{GREEN}\nIngrese el nombre o id del pokemon a buscar: {RESET}')).lower().replace(" ","-") # El usuario ingresa el nombre del pokemon, luego este se coloca en minuscula
    try:
        # El usuario ingresa el pokemon por ID
        id_pokemon = int(input_pokemon)
        pokemon = pb.pokemon(id_pokemon)
    except Exception as e:
        try:
            # EL usuario ingresa el pokemon por nombre, de igual forma guardamos el ID
            pokemon = pb.pokemon(input_pokemon)
            id_pokemon = pokemon.id
        except Exception as e:
            print(f'\n{MAGENTA}Error, pokemon \'{input_pokemon}\' no encontrado!!!{RESET}')
            menu_principal()  
    
    opcion_pokemon = None
    
    # Se utiliza el ID para apuntar al archivo GIF del Pokemon
    gif_dir = os.path.dirname(__file__)
    ruta_gif = os.path.join(gif_dir,'showdown',f'{id_pokemon}.gif')
    pokemon_image = from_file(ruta_gif)
    print('')
    pokemon_image.draw(repeat=1)
    
    while opcion_pokemon != 6:
        print(f'''{GREEN}\nOpciones de Pokemon: \n{RESET} 
1. Habilidades
2. Experiencia Base
3. Longitud y peso
4. Tipo
5. Estadisticas
6. Salir al menu principal''')

        while True:
            try:
                opcion_pokemon = int(input(f'{GREEN}\nIngrese que atributo quiere ver de{RESET} {YELLOW}{(pokemon.name).replace('-',' ').capitalize()}{RESET}{GREEN}: {RESET}'))
                break
            except Exception as e:
                print(f'\n{MAGENTA}No es una opcion valida, favor seleccione valores del 1-5 !!!{RESET}')
        if opcion_pokemon == 1: # Selecciona la opcion de ver habilidades
            movimientos = [move.move.name for move in pokemon.moves]
            print(f'\n{GREEN}Movimientos de{RESET} {YELLOW}{(pokemon.name).capitalize()}{RESET}:\n{'\n'.join(movimientos).replace('-',' ')}')
            # Se utiliza replace para quitar los parametros "-" o "--" de los movimientos           
        
        elif opcion_pokemon == 2: # Seleciona experencia base
            experiencia_base = pokemon.base_experience
            print(f'\nLa experiencia base de {GREEN}{(pokemon.name).capitalize()}{RESET} es {YELLOW}{experiencia_base}{RESET}')
        elif opcion_pokemon == 3: # Seleciona la altura y peso
            altura_pokemon = pokemon.height
            peso_pokemon = pokemon.weight
            print(f'\nLa longitud de {GREEN}{(pokemon.name).capitalize()}{RESET} es {YELLOW}{altura_pokemon * 10} CM{RESET} y su peso es de {YELLOW}{peso_pokemon / 10}kg{RED}') 
            # La PokeAPI da los balores en decimetros,
            # por ello lo multiplicamos por 10 para mostrar en cm
        elif opcion_pokemon == 4:
            tipo_pokemon = pokemon.types
            if len(tipo_pokemon) == 2: # Si el pokemon tiene dos tipos
                #type1 = tipo_pokemon[0]
                #type2 = tipo_pokemon[1]
                print(f'\n{GREEN}{(pokemon.name).capitalize()}{RESET} es tipo {YELLOW}{(tipo_pokemon[0]).type.name}{RESET} y {YELLOW}{(tipo_pokemon[1]).type.name}{RESET}')
            elif len(tipo_pokemon) == 1: # Si el pokemon tiene un solo tipo
                type1 = tipo_pokemon[0]
                print(f'\n{GREEN}{(pokemon.name).capitalize()}{RESET} es tipo {YELLOW}{(type1.type.name).capitalize()}{RESET}')
        elif opcion_pokemon == 5:
            estadisticas = [(f'{estadistica.stat.name,estadistica.base_stat}'.replace('\'',"").replace(',',':').strip('()').capitalize()) for estadistica in pokemon.stats]          
            print(f'\n{GREEN}Estadisticas de {RESET}{YELLOW}{(pokemon.name).capitalize()}{RESET}{GREEN}:{RESET}\n{'\n'.join(estadisticas).replace("-"," ")}')
        elif opcion_pokemon == 6:
            menu_principal()
        else:
            print(f'\n{MAGENTA}No es una opcion valida, favor seleccione valores del 1-5 !!!{RESET}')

def listar_tipos():
     lista_tipos = [pb.type_(tipo).name for tipo in range(1,20)]
     print(f'\nTipos de Pokemon:\n{'\n'.join(lista_tipos)}')

def buscar_movimientos():

    opcion_movimientos = None
        
    while opcion_movimientos != 3:
        print(f'''{GREEN}\nElige una opcion de busqueda:{RESET}\n
1. Buscar por nombre
2. Listar movimientos por tipo
3. Salir al menu principal''')
        
        while True:
            try:
                opcion_movimientos = int(input(f'\n{GREEN}Ingrese una opcion: {RESET}'))
                break
            except Exception as e:
                print(f'\nNo es una opcion valida, favor seleccione los valores del 1-3 !!!')
                buscar_movimientos()

        
        if opcion_movimientos == 1: # Buscar por nombre
            
            input_movimiento = (input(f'{GREEN}\nIngresa el nombre del movimiento: {RESET}')).lower().replace(' ','-') # Ingresa el nombre del movimiento y se coloca todo a minusculas
            try:
                movimiento = pb.move(input_movimiento)
                _ = movimiento.id
            except Exception as e:
                print(f'Movimiento \'{movimiento}\' no encontrado ')
                continue
            
            try:              
                mov_es = (movimiento.names[5])
                print(f'''\nAtributos del movimiento {movimiento.name}\n
{GREEN}Nombre en español:{RESET} {mov_es.name}
{GREEN}Descripcion:{RESET} {(movimiento.flavor_text_entries[0].flavor_text.replace('\n',' '))}
{GREEN}Precision:{RESET} {movimiento.accuracy}
{GREEN}Poder:{RESET} {movimiento.power}
{GREEN}PP:{RESET} {movimiento.pp}
{GREEN}Tipo:{RESET} {movimiento.type}''')
            except Exception as e:
                print(f'''\nAtributos del movimiento {movimiento.name}\n
{GREEN}Descripcion:{RESET} {(movimiento.flavor_text_entries[0].flavor_text.replace('\n',' '))}
{GREEN}Precision:{RESET} {movimiento.accuracy}
{GREEN}Poder:{RESET} {movimiento.power}
{GREEN}PP:{RESET} {movimiento.pp}
{GREEN}Tipo:{RESET} {movimiento.type}''')
            
            while True:
                opcion = (input(f'Ver los Pokemones que pueden aprender {movimiento.name} (Si-No)?: ')).lower()
                try:
                    if opcion == 'si':
                        learned_pokemon = [poke_.name for poke_ in movimiento.learned_by_pokemon]                
                        print(f'\nPokemones que aprenden {(movimiento.name).replace('-',' ')}:\n{'\n'.join(learned_pokemon).replace('-',' ')}\n')
                        break
                    elif opcion == 'no':
                        break
                except Exception as e:
                    print('Por favor eliga una opcion valida (Si-No)')

        elif opcion_movimientos == 2: # Lista movimientos por tipo
            
            while True:
                input_movimiento = (input(f'\n{GREEN}Ingresa el tipo de movimientos a listar: {RESET}')).lower()
                tipos_movimientos = pb.type_(input_movimiento)
                try:
                    _ = tipos_movimientos.id
                    break
                except Exception as e:
                    print(f'\nTipo {input_movimiento} no valido!!!')
                    buscar_movimientos()
            list_movimientos = [move.name for move in tipos_movimientos.moves]
            print(f'\nMovimientos tipo {YELLOW}{input_movimiento.capitalize()}{RESET}: {'\n'.join(list_movimientos).replace('-',' ').replace("  "," ")}')
        elif opcion_movimientos == 3: 
            menu_principal()
        else:
            print(f'\nNo es una opcion valida, favor seleccione los valores del 1-3 !!!\n')
            buscar_movimientos()

def menu_principal():
    
    opciones_menu_principal = None

    while opciones_menu_principal != 4:
        
        print(f'{GREEN}{text2art('poke cli')}{RESET}')
        
        print(f'''
        {GREEN}Menu de opciones:{RESET}

1. Buscar Pokemon por nombre o id y ver atributos
2. Listar tipos de Pokemon
3. Buscar movimientos
4. Salir''')
        
        while True:
            try:
                opciones_menu_principal = int(input(f'{GREEN}\nEliga una opcion (1-4): {RESET}')) # El usuario elige una opcion del menu
                break
            except Exception as e:
                print(f'\nNo es una opcion valida, favor seleccione valores del 1-4')
        
        if opciones_menu_principal == 1: # Se verifica que la opcion elegida sea la de buscar un Pokemon por nombre
            buscar_pokemon()
        elif opciones_menu_principal == 2: # Se elige la opcion de mostrar los tipos de Pokemon
            listar_tipos()
        elif opciones_menu_principal == 3: # Se elige la opcion de buscar movimientos
            buscar_movimientos()
        elif opciones_menu_principal == 4: # Se elige la opcion de salir del programa
            exit()


menu_principal()
