import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
import csv
import os


sg.theme('Python')

sg.theme('Python')

path_files = "Datos"
archivo_puntajes = "prueba_puntajes.csv"
path_arch = os.path.join(os.getcwd(), path_files)

with open(os.path.join(path_arch, archivo_puntajes)) as arch_puntajes:
    data_puntajes = csv.reader(arch_puntajes, delimiter = ',')
    header , puntajes = next(data_puntajes), list(data_puntajes)

def obtener_lista_jugadores_por_dificultad(cabecera, data, dificultad):
    lista_jugadores = list(filter(lambda x: x[cabecera.index("nationality")] == dificultad, data))
    lista_jugadores = list(map(lambda x : [int(x[cabecera.index("player_id")]), x[cabecera.index("name")]], lista_jugadores))
    return sorted(lista_jugadores, key=lambda x: x[0], reverse=True)[:20]

def crear_listbox_por_dificultad(cabecera, datos, dificultad):
    return sg.Listbox(obtener_lista_jugadores_por_dificultad(cabecera, datos, dificultad), size=(30, 20), no_scrollbar=True)


def crear_ventana_puntajes(cabecera, datos):
    column1 = [[sg.Text('Fácil', size=(30, 1))],
            [crear_listbox_por_dificultad(cabecera, datos, "Facil")],
            [sg.Text('Medio', size=(30, 1))],
            [crear_listbox_por_dificultad(cabecera, datos, "Medio")]
            ]
    column2 = [[sg.Text('Dificil', size=(30, 1))],
            [crear_listbox_por_dificultad(cabecera, datos, "Dificil")],
            [sg.Text('Experto', size=(30, 1))],
            [crear_listbox_por_dificultad(cabecera, datos, "Experto")]
            ]


    layout = [[sg.Text('Ranking de los mejores 20 puntajes para cada dificultad', font='Helvetica 12 bold italic')], [sg.Column(column1), sg.Column(column2)],[sg.Button('Volver', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PUNTAJES-VOLVER-")]] 
    return sg.Window("Puntajes", layout, finalize=True)

def mostrar_ventana_puntajes(cabecera, datos):
    crear_ventana_puntajes(cabecera, datos)

    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Ventana actual: {current_window}, Evento: {event}, valores: {values}")
        if event in (sg.WIN_CLOSED, "-PUNTAJES-VOLVER-"):
            menu.crear_ventana_principal()
            current_window.close()
            break
        # Indicar eventos de cada boton a utilizar en esta ventana

if __name__ == "__main__":
    mostrar_ventana_puntajes(header,puntajes)
