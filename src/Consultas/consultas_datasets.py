import csv
import os
from random import choice


def obtener_nombre_dataset_aleatorio():
    path_files = "Datasets"
    path_arch = os.path.join(os.getcwd(), path_files)
    lista_data_sets = os.listdir(path_arch)
    categoria = choice(lista_data_sets)
    return categoria


def abrir_dataset(nombre_archivo, delimiter=';'):
    path_files = "Datasets"
    archivo_a_abrir = nombre_archivo
    path_arch = os.path.join(os.getcwd(), path_files)
    try:
        with open(os.path.join(path_arch, archivo_a_abrir), encoding="utf-8") as archivo:
            data_archivo = csv.reader(archivo, delimiter=delimiter)
            header, data = next(data_archivo), list(data_archivo)
        return header, data
    except FileNotFoundError as no_hay_archivo:
        print(f'El archivo a procesar no se encuentra en la ruta especificada, error: {no_hay_archivo}')


def seleccionar_linea_al_azar(datos):
    lineas = datos.splitlines()
    return choice(lineas)

