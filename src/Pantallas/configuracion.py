"""
El módulo de configuración de Figurace.py consta de 2 partes principales:

1- Lógica de pantalla y Manipulación de eventos/Ventana (Sólo buscamos manejar el tiempo por ronda
    y cantidad de rondas cómo eventos independientes por ser botones)
2- Generar y modificar nuestro archivo de configuración principal a lo largo del juego,
   el cuál se genera con campos por defecto en la función:crear_archivo_configuracion_json()
PD: Para "generar orden" se crea un archivo de configuracion "config.json" en el directorio "config"
"""

import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
import os
import json

sg.theme('Python')


def crear_ventana_configuracion():
    """
    Devuelve ventana de configuración.
    Son consumidos los valores del arch. de configuración json. con valores por defecto
    """
    if not os.path.exists(get_json_route()) or os.stat(get_json_route()).st_size <= 1:
        crear_archivo_configuracion_json()

    data = json.load(open(get_json_route()))
    print(data)

    #Elegí que la seleccion del numero de rondas y tiempo sea devuelto en una cadena
    layout = [
            [sg.Text('Pantalla de configuración principal', size=(0, 1))],
            [sg.Text('Ingrese tiempo por ronda:', size=(30, 1)), sg.Button('25 s', key='-EASY-TIME-'), sg.Button('20 s', key='-MEDIUM-TIME-'), sg.Button('17 s', key='-HARD-TIME-'), sg.Button('15 s', key='-EXPERT-TIME-')],
            [sg.Text('Ingrese numero de rondas a jugar:', size=(30, 1)), sg.Button('3', key='-EASY-LEVEL-'), sg.Button('4', key='-MEDIUM-LEVEL-'), sg.Button('5', key='-HARD-LEVEL-')],
            [sg.Text('Ingrese puntos a sumar por acierto:', size=(30, 1)), sg.InputText(data['-POINTS_TO_ADD-'], key='-POINTS_TO_ADD-')],
            [sg.Text('Ingrese puntos a restar por error:', size=(30, 1)), sg.InputText(data['-POINTS_TO_SUBB-'], key='-POINTS_TO_SUBB-')],
            [sg.Text('Características a ver por ronda:', size=(30, 1)), sg.InputText(data['-TOTAL_CHARS-'], key='-TOTAL_CHARS-')],
            [sg.Button('Guardar configuración', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=1, key="-SAVE-CHANGES-"), sg.Button('Volver', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-CONFIGURACION-VOLVER-")],
            ]
    return sg.Window('Pantalla de configuración', layout, finalize=True)


def crear_archivo_configuracion_json():
    """
    Crea Archivo de Configuraación con los datos solicitados: Tiempo Limite por ronda, Número de rondas,
     puntos a sumar y restar y total de características (columnas) a consumir por dataset
     Esta función debe ser invocada antes de invocar a la sig. update_main..
    """

    data = {'-LIMIT_TIME-': 25, '-ROUNDS-': 2, '-POINTS_TO_ADD-': 10, '-POINTS_TO_SUBB-': 5, '-TOTAL_CHARS-': 3}
    with open(get_json_route(), 'w') as file:
        file.write(json.dumps(data, indent=4))


def update_main_configuration(time_in_sec, rounds, event):
    """
    Recibe como argumento los últimos dos valores por defecto asociados en el archivo JSON
    y el evento correspondiente
    """
    data = {}
    with open(get_json_route(), 'r') as file:
        data = json.load(file)
    data.update(event)
    if time_in_sec != -1:
        data['-LIMIT_TIME-'] = time_in_sec
    if rounds != -1:
        data['-ROUNDS-'] = rounds
    with open(get_json_route(), 'w') as file:
        json.dump(data, file, indent=4)


def get_json_route():
    """
    Devuelve la ruta del archivo de configuración principal de figurace.py
    """
    path_father = os.path.dirname(os.path.abspath(__file__)).replace('Pantallas', '')
    route_file = os.path.join(path_father, 'config', 'config.json')
    return route_file


def update_time(event):
    """
    Retorna el tiempo a devolver si se genera un evento de tipo boton (relacionado al tiempo)
    """
    if event == "-EASY-TIME-":
        return 25
    elif event == "-MEDIUM-TIME-":
        return 20
    elif event == "-HARD-TIME-":
        return 17
    elif event == "-EXPERT-TIME-":
        return 15


def update_rounds(event):
    """
       Retorna el total de rondas a jugar, si se genera un evento de tipo boton (relacionado al numero de rondas)
   """
    if event == "-EASY-LEVEL-":
        return 3
    elif event == "-MEDIUM-LEVEL-":
        return 4
    elif event == "-HARD-LEVEL-":
        return 5


def mostrar_ventana_configuracion():
    """
        Funcion que muestra la pantalla del menu de configuracion del juego y establece sus funcionalidades
    """
    crear_ventana_configuracion()
    time = -1
    rounds = -1
    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Ventana actual: {current_window}, Evento: {event}, valores: {values}")
        if event in (sg.WIN_CLOSED, "-SAVE-CHANGES-", "-CONFIGURACION-VOLVER-"):
            if event == "-SAVE-CHANGES-":
                update_main_configuration(time, rounds, values)
            menu.crear_ventana_principal()
            current_window.close()
            break
        if "TIME" in event:
            time = update_time(event)
        elif "LEVEL" in event:
            rounds = update_rounds(event)

