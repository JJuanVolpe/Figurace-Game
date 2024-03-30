import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
import csv
import os

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
    
def crear_ventana_puntajes(lista_jugadores):
    sg.set_options(element_padding=(0, 0))
    col1 = [[sg.Table(values=lista_jugadores,
                        headings=["Puntajes", "Nombre"],
                        max_col_width=25,
                        auto_size_columns=True,
                        justification='right',
                        # alternating_row_color='lightblue',
                        num_rows=min(len(lista_jugadores), 20), key='-TABLA-PUNTAJES-')],
            [sg.Button('Volver', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PUNTAJES-VOLVER-")]]
    col2 = [[sg.Combo(values=["Facil", "Medio", "Dificil", "Experto"], readonly=True, key='-COMBO-PUNTAJES-', size=(10,3))],
    [sg.Button('Ok', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PUNTAJES-OK-", bind_return_key=True)]]
    
    layout = [[sg.Column(col1), sg.Column(col2)]] 
    return sg.Window("Puntajes", layout, finalize=True)

def actualizar_ventana(ventana_anterior, cabecera, data, dificultad):
    ventana_anterior['-TABLA-PUNTAJES-'].update(obtener_lista_jugadores_por_dificultad(cabecera, data, dificultad))


def mostrar_ventana_puntajes(header, puntajes):
    lista = obtener_lista_jugadores_por_dificultad(header, puntajes, "Facil")
    window = crear_ventana_puntajes(lista)

    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Ventana actual: {current_window}, Evento: {event}, valores: {values}")
        if event in (sg.WIN_CLOSED, "-PUNTAJES-VOLVER-"):
            menu.crear_ventana_principal()
            current_window.close()
            break
        elif event == "-PUNTAJES-OK-":
            actualizar_ventana(window, header, puntajes, values['-COMBO-PUNTAJES-'])

if __name__ == "__main__":
    mostrar_ventana_puntajes()