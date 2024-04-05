import PySimpleGUI as sg
import Menu_Inicio_Juego as menu
from Consultas import consultas_usuarios 


sg.theme('Python')

def crear_ventana_perfil():
    """
        Funcion que define los elementos que tendra la pantalla de perfil
    """
    layout =  [
        [sg.Button('Crear Perfil', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PERFIL-CREAR-PERFIL-")],
        [sg.Button('Modificar Perfil', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PERFIL-MODIFICAR-PERFIL-")],
        [sg.Button('Volver', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), border_width=0, key="-PERFIL-VOLVER-")]
    ]
    return sg.Window("Perfil", layout, finalize=True)

def crear_ventana_creacion_perfil():
    """
        Funcion que define los elementos que contendra la ventana de 
        creacion de perfil y retorna la misma
    """
    layout = [
        [sg.Text('Ingrese su nick, edad y genero autopercibido')],
        [sg.Text("Nick", size=(15,1)), sg.Input(key='-NICK-')], 
        [sg.Text("Edad", size=(15,1)), sg.InputText(key='-EDAD-')],
        [sg.Text("Genero autopercibido", size=(15,1)), sg.InputText(key='-GENERO AUTOPERCIBIDO-')],
        [sg.B('Confirmar datos',  font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), key="-PERFIL-CREAR PERFIL-CONFIRMAR DATOS-"),
        sg.B('Cancelar', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), key="-PERFIL-CREAR PERFIL-CANCELAR-")]
    ]
    return sg.Window("Creando Perfil", layout, finalize=True)


def crear_ventana_modificacion_perfil():
    layout = [
        [sg.Text('Ingrese los datos a actualizar')], 
        [sg.Text("Nueva edad", size=(15,1)), sg.InputText(key='-EDAD NUEVA-')],
        [sg.Text("Nuevo genero autopercibido", size=(15,1)), sg.InputText(key='-GENERO AUTOPERCIBIDO NUEVO-')],
        [sg.B('Confirmar cambios',  font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), key="-PERFIL-CREAR PERFIL-CONFIRMAR DATOS-"),
        sg.B('Cancelar', font='Helvetica 12 bold italic', button_color=('white', sg.theme_background_color()), key="-PERFIL-MODIFICAR PERFIL-CANCELAR-")]
    ]
    return sg.Window("Creando Perfil", layout, finalize=True)

def mostrar_ventana_perfil(usuario_actual):
    crear_ventana_perfil()
    while True:
        current_window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, "-PERFIL-VOLVER-"):
            menu.crear_ventana_principal()
            current_window.close()
            break
        elif event == "-PERFIL-CREAR-PERFIL-":
            crear_ventana_creacion_perfil()
            current_window.close()
        elif event == "-PERFIL-CREAR PERFIL-CONFIRMAR DATOS-":
            consultas_usuarios.agregar_perfil(values['-NICK-'], values['-EDAD-'], values['-GENERO AUTOPERCIBIDO-'])
            crear_ventana_perfil()
            current_window.close()
        elif event == "-PERFIL-MODIFICAR-PERFIL-":
            crear_ventana_modificacion_perfil()
            current_window.close()    
        elif event == "-PERFIL-MODIFICAR DATOS-CONFIRMAR DATOS-":
            consultas_usuarios.modificar_perfil(usuario_actual, values['-EDAD NUEVA-'], values['-GENERO AUTOPERCIBIDO NUEVO-'])        
            crear_ventana_perfil()
            current_window.close()        
        elif event in ("-PERFIL-CREAR PERFIL-CANCELAR-", "-PERFIL-MODIFICAR PERFIL-CANCELAR-"):
            crear_ventana_perfil()
            current_window.close()    

if __name__ == "__main__":
    mostrar_ventana_perfil()
