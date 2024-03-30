import PySimpleGUI as sg
import juego, configuracion, perfil, puntajes

sg.theme('Python')

lista_jugadores = ["Sirius", "Pepito"]
lista_dificultades = ["Facil", "Normal", "Dificil", "Experto"]

def crear_botones_ventana_principal():
    """
        Funcion que crea los botones que tendra la ventana principal del juego, ademas de las
        opciones para elegir usuario y dificultad
    """
    col1 = [
    [sg.Button('Jugar', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PRINCIPAL-JUEGO-")],
    [sg.Button('Configuracion', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PRINCIPAL-CONFIGURACION-")],
    [sg.Button('Puntajes', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PRINCIPAL-PUNTAJES-")],
    [sg.Button('Perfil', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PRINCIPAL-PERFIL-")],
    [sg.Button('Salir', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PRINCIPAL-SALIR-")]
    ]
    col2 = [
        [sg.Combo(values=lista_jugadores, default_value="Usuarios", readonly=True, k='-COMBO-USUARIOS-', size=(10,3))], 
        [sg.Combo(values=lista_dificultades, default_value="Dificultad", readonly=True, k='-COMBO-DIFICULTAD-')]
    ]
    return [col1, col2] 

def crear_ventana_principal():
    """
        Funcion que devuelve la pantalla del menu principal del juego
    """
    botones = crear_botones_ventana_principal()
    layout = [[sg.Push(), sg.Column(botones[0]), sg.Column(botones[1]), sg.Push()]]
    return sg.Window("Ventana principal", layout, finalize=True)

def mostrar_ventana_principal():
    """
        Funcion que muestra la pantalla del menu del juego y establece sus funcionalidades
    """
    crear_ventana_principal()    

    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Ventana actual: {current_window}, Evento: {event}, valores: {values}")
        if event in (sg.WIN_CLOSED, "-PRINCIPAL-SALIR-"):
            current_window.close()
            break
        elif event == "-PRINCIPAL-JUEGO-":
            juego.mostrar_ventana_juego()
            current_window.close()
        elif event == "-PRINCIPAL-CONFIGURACION-":
            configuracion.mostrar_ventana_configuracion()
            current_window.close()
        elif event == "-PRINCIPAL-PUNTAJES-":
            puntajes.mostrar_ventana_puntajes()
            current_window.close()
        elif event == "-PRINCIPAL-PERFIL-":
            perfil.mostrar_ventana_perfil(values['-COMBO-USUARIOS-'])
            current_window.close()        

if __name__ == "__main__":
    mostrar_ventana_principal()    

