import json
import PySimpleGUI as sg
import os

def crear_json_perfiles(dicci):
    """
        Funcion que crea el archivo json con la informacion solicitada
        a los usuarios (nick, edad y genero autopercibido) 
    """
    with open("perfiles.json", "w") as arch_perfiles:
        json.dump([dicci], arch_perfiles)


def agregar_usuario(data, dicci, arch_perfiles):
    data.append(dicci)
    arch_perfiles.seek(0)
    json.dump(data, arch_perfiles)


def agregar_perfil_a_archivo(dicci):
    """
        Funcion que agrega inforacion de un usuario al archivo json. En 
        caso de que el nick ingresado por el usuario ya exista, se muestra
        un cartel de error avisando al usuario que el nick ingresado ya existe.
        En caso contrario, se crea el perfil del usuario
    """
    with open("perfiles.json", "r+") as arch_perfiles:
        data = json.load(arch_perfiles)
        try:
            lista_nicks = map(lambda item: item['Nick'], data)
            raise ValueError if dicci["Nick"] in lista_nicks else agregar_usuario(data, dicci, arch_perfiles)
        except ValueError:
            sg.popup_error('El nick ingresado ya existe, por favor ingrese otro')


def agregar_perfil(nick, edad, genero_autopercibido):
    dicci = {"Nick": nick, "Edad": edad, "Genero autopercibido": genero_autopercibido}
    crear_json_perfiles(dicci) if os.path.isfile('perfiles.json') else agregar_perfil_a_archivo(dicci, nick)


def modificar_perfil(nick_a_modificar, nueva_edad, nuevo_gen_autopercibido):
    with open("perfiles.json", "w") as arch_perfiles:
        data = json.load(arch_perfiles)
        indice = next((i for i, x in enumerate(data) if x["Nick"] == nick_a_modificar), None)
        data.index(indice)["Edad"] = nueva_edad
        data.index(indice)["Genero autopercibido"] = nuevo_gen_autopercibido
