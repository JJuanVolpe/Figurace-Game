import os.path
import re
from consultas_datasets import *
import csv

def route_csv_file_to_work():
    """Devuelve ruta del archivo csv a procesar (incluyendo nombre)
    """
    path_file = os.path.join(os.getcwd(), 'Datasets', 'Lagos Argentina.csv')
    return path_file


def route_new_file():
    """Devuelve ruta ESTIMADA de nuevo archivo csv (incluyendo nombre)
    """
    path_file = os.path.join(os.getcwd(), 'Datasets', 'Lagos Argentina Modificado.csv')
    return path_file


def exists_new_file():
    """Retorna true si existe el data-set de lagos generado con las especificaciones solicitadas
    """
    route_of_new_dataset = route_new_file()
    return os.path.exists(route_of_new_dataset)


def evaluate_coordinates(line):
    """Se calcula longitud y latitud, retornando el campo de coordenadas modificado
        Conversión de Coordenadas: se asumió una conversión del sistema DMS al DD (grados)
        Comprobé la conversión en: http://maps.marnoto.com/es/conversor-coordenadas/
    """
    a = re.split(r'[°\"\'"SO]+', line[4])  # Filtro columna de coordenadas,obteniendo numeros con latitud y longitud :)
    del a[6]  # a[6]= ''
    a = list(map(lambda x: int(x), a))
    latitud = str(a[0] + ((a[1]) / 60) + (a[2] / 3600))[0:5] + '°S, '
    longitud = str(a[3] + (a[4] / 60) + (a[5] / 3600))[0:5] + '°W'
    aux = latitud + longitud
    line[4] = aux


def process_csv_data(reader_csv_data, writer):
    """Escribiendo nuevo contenido en orden específico,teniendo en cuenta irregularidades del data-set
    """
    for line in reader_csv_data:
        line.append(line.pop(0))
        evaluate_empty_fields(line)
        evaluate_coordinates(line)
        writer.writerow(line)


def evaluate_empty_fields(line):
    """Rellena campos vacíos del dataset"""
    if '' == line[2]:  # Posición relativa a Profundidad Media (m)
        line[2] = 'Desconocido'
    if '' == line[3]:  # Posición relativa a Profundidad Máxima (m)
        line[3] = 'Desconocido'


def obtain_csv_dataset():
    """Esta funcion recibe el dataset referente a lagos, y crea una copia con modificaciones solicitados en formato csv
    """
    path_new_file = route_new_file()
    data_set_titles, data_set = abrir_dataset('Lagos Argentina.csv', ',')
    data_set_titles.append(data_set_titles.pop(0))
    with open(path_new_file, 'w') as new_csv:
        writer = csv.writer(new_csv)
        writer.writerow(data_set_titles)
        process_csv_data(data_set, writer)


def generate_csv():
    """Genera el dataset de lagos o retorna mensaje en consola si se haya creado"""
    try:
        obtain_csv_dataset()
    except FileExistsError as error:
        print(f'Existe el csv que desea generar, => {error.__str__()}')
    except FileNotFoundError as not_found_f:
        print(f'No se ha hallado un archivo existente, error:{not_found_f}')


if __name__ == "__main__":
    generate_csv()
