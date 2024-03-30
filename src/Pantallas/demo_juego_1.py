import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
from numpy import random
import os


sg.theme('Python')

path_files = "Datos/Data sets"
path_arch = os.path.join(os.getcwd(), path_files)
lista_data_sets = os.listdir(path_arch)
categoria = random.choice(lista_data_sets)

with open(os.path.join(path_arch, categoria)) as cat:
    
    cat.seek(0)
    header_line = cat.readline()
    header = header_line.split(';')
    
    rowcount  = 0
    for row in cat: 
        rowcount+= 1
    filesize = rowcount 
    offset = random.randrange(filesize)

    cat.seek(offset)
    cat.readline()                   

    random_line_1 = cat.readline()
    opcion_1 = random_line_1.split(';')

    random_line_2 = cat.readline()
    opcion_2 = random_line_2.split(';')

    random_line_3 = cat.readline()
    opcion_3 = random_line_3.split(';')

    random_line_4 = cat.readline()
    opcion_4 = random_line_4.split(';')

    random_line_5 = cat.readline()
    opcion_5 = random_line_5.split(';')

    print('opcion 1:', opcion_1)
    print('opcion 2:', opcion_2)
    print('opcion 3:', opcion_3)
    print('opcion 4:', opcion_4)
    print('opcion 5:', opcion_5)

    lista_opciones = [opcion_1, opcion_2, opcion_3, opcion_4, opcion_5]
    
    opcion_adivinar = random.choice(lista_opciones)
    print('opcion correcta:', opcion_adivinar)

def crear_ventana_juego(values):
    
    puntaje_partida = 0
    dicci_rondas = {}
    
    for ronda in range(1, ['-ROUNDS-'] + 1):


        column1 = [[sg.Text('Categoría', values['-CATEGORIA-'], font='Helvetica 12 bold italic')],
                   [sg.Text('Dificultad', values['-DIFICULTAD-'], font='Helvetica 12 bold italic')],
                   [sg.HorizontalSeparator()],
                   [sg.Text('Perfíl =', values['-NICK-'], font='Helvetica 12 bold italic')],
                   [sg.Text('Rondas =', values[ronda],'/', values['-ROUNDS-'], font='Helvetica 12 bold italic')],
                   [sg.Text('puntaje actual =', values[puntaje_partida], font='Helvetica 12 bold italic')],
                   [sg.Multiline(size=(5,10), font='Helvetica 12 bold italic', key='-STLINE-', autoscroll=True)] #Agregar acierto y no aciertos
                   [sg.Button('Abandonar', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-JUEGO-ABANDONAR-")]
                   ]
        column2 = [[sg.Text(f'{header[0]} = {opcion_adivinar[0]}', font='Helvetica 12 bold italic')],
                   [sg.Text(f'{header[1]} = {opcion_adivinar[1]}', font='Helvetica 12 bold italic')],
                   [sg.Text(f'{header[2]} = {opcion_adivinar[2]}', font='Helvetica 12 bold italic')],
                   [sg.Text(f'{header[3]} = {opcion_adivinar[3]}', font='Helvetica 12 bold italic')],
                   [sg.Text(f'{header[4]} = {opcion_adivinar[4]}', font='Helvetica 12 bold italic')],
                   [sg.Text(f'{header[5]} = ¿?', font='Helvetica 12 bold italic', text_color='red')],
                   [sg.HorizontalSeparator()],
                   [sg.Button('OPCION 1', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-OPCION-1-")],
                   [sg.Button('OPCION 2', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-OPCION-2-")],
                   [sg.Button('OPCION 3', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-OPCION-3-")],
                   [sg.Button('OPCION 4', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-OPCION-4-")],
                   [sg.Button('OPCION 5', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-OPCION-5-")],
                   [sg.Button('PASAR', font='Helvetica 12 bold italic', button_color=('red', sg.theme_background_color()), border_width=0, key="-JUEGO-PASAR-")]
                   ]


        layout = [[sg.Text('Pantalla de Juego', font='Helvetica 12 bold italic')], 
                  [sg.Column(column1), sg.VerticalSeparator(), sg.Column(column2)]
                 ]


        if event in ("-OPCION-1-"):
            if opcion_1 == opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_ADD-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'Acierto'
            else:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break
                  
        elif event in ("-OPCION-2-"):
            if opcion_2 = opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_ADD-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'Acierto'
            elif:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break
                  
        elif event in ("-OPCION-3-"):
            if opcion_3 = opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_ADD-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'Acierto'
            elif:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break
                  
        elif event in ("-OPCION-4-"):
            if opcion_4 = opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_ADD-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'Acierto'
            elif:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break
                  
        elif event in ("-OPCION-5-"):
            if opcion_5 = opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_ADD-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'Acierto'
            elif:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break

        elif event in ("-JUEGO-PASAR-"):
            if opcion_5 = opcion_adivinar:
                puntaje_partida = puntaje_partida + data{['-POINTS_TO_SUBB-']}
                dicci_rondas[f'Ronda {ronda}:'] = 'No acierto'
            break
                  
    path_files_2 = "Datos/puntajes_prueba.csv"
    path_arch_2 = os.path.join(os.getcwd(), path_files_2)
                  
    with open(path_arch_2,'w', encoding='utf8') as puntajes_salida:
        writer = csv.writer(puntajes_salida)
        writer.writerow(puntaje_partida,['-NICK-'],['-DIFICULTAD-'])
     
    return sg.Window('Juego', layout, finalize=True)

def mostrar_ventana_juego():
    crear_ventana_juego(values)

    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Ventana actual: {current_window}, Evento: {event}, valores: {values}")
        if event in (sg.WIN_CLOSED, "-JUEGO-ABANDONAR-"):
            menu.crear_ventana_principal()
            current_window.close()
            break
        # Indicar eventos de cada boton a utilizar en esta ventana

if __name__ == "__main__":
    mostrar_ventana_juego()
