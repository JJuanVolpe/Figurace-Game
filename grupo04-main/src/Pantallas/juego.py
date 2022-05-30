import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
from Consultas import consultas_datasets
from random import choice

sg.theme('Python')

def obtener_categoria_y_opciones():
    categoria = consultas_datasets.obtener_nombre_dataset_aleatorio()
    header, datos = consultas_datasets.abrir_dataset(categoria)  
    lista_opciones = [consultas_datasets.seleccionar_linea_al_azar(datos) for i in range(4)]
    return header, categoria, lista_opciones

def crear_texto_caracteristicas(header, lista_opciones, num_caracteristica):
    return sg.Text(f'{header[num_caracteristica]} = {lista_opciones[num_caracteristica]}', font='Helvetica 12 bold italic')

def obtener_listado_caracteristicas(header, lista_opciones):
    return [crear_texto_caracteristicas(header, lista_opciones, car) for car in range(4)]

def crear_ventana_juego():
    """
        Funcion que crea la ventana de creacion/modiicacion de perfil
    """
    categoria, lista_opciones = obtener_categoria_y_opciones()
    column1 = [[sg.Text('Categoría', values['-CATEGORIA-'], font='Helvetica 12 bold italic')],
                [sg.Text('Dificultad', values['-DIFICULTAD-'], font='Helvetica 12 bold italic')],
                [sg.HorizontalSeparator()],
                [sg.Text('Perfíl =', values['-NICK-'], font='Helvetica 12 bold italic')],
                [sg.Text('Rondas =', values[ronda],'/', values['-ROUNDS-'], font='Helvetica 12 bold italic')],
                [sg.Text('puntaje actual =', values[puntaje_partida], font='Helvetica 12 bold italic')],
                [sg.Multiline(size=(5,10), font='Helvetica 12 bold italic', key='-STLINE-', autoscroll=True)] #Agregar acierto y no aciertos
                [sg.Button('Abandonar', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-JUEGO-ABANDONAR-")]
                ]
    column2 = [[sg.Text(f'{header[0]} = {lista_opciones[0]}', font='Helvetica 12 bold italic')],
                [sg.Text(f'{header[1]} = {lista_opciones[1]}', font='Helvetica 12 bold italic')],
                [sg.Text(f'{header[2]} = {lista_opciones[0]}', font='Helvetica 12 bold italic')],
                [sg.Text(f'{header[3]} = {lista_opciones[0]}', font='Helvetica 12 bold italic')],
                [sg.Text(f'{header[4]} = {lista_opciones[0]}', font='Helvetica 12 bold italic')],
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

    return sg.Window("Juego", layout, finalize=True)

def mostrar_ventana_juego():
    crear_ventana_juego()

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