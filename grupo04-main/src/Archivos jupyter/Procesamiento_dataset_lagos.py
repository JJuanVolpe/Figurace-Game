import csv
import os.path
import re
import sys

def route_new_file():
    """Devuelve ruta ESTIMADA de nuevo archivo csv (incluyendo nombre)
    """
    path_file = os.path.join(os.getcwd(), 'datasets/new_data_set.csv')
    return path_file


def route_csv_file_to_work():
    """Devuelve ruta del archivo csv a procesar (incluyendo nombre)
    """
    path_file = os.path.join(os.getcwd(), 'datasets/Lagos Argentina.csv')
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
    a = re.split(r'[!°\'"SO]+', line[4])  # Filtro columna de coordenadas,obteniendo numeros con latitud y longitud :)
    del a[6]  # Ultimo espacio de lista vacio a[6]= ''  ? Innecesario si acomodamos el re.split()
    a = list(map(lambda x: int(x), a))
    latitud = str(a[0] + ((a[1]) / 60) + (a[2] / 3600))[0:5] + '°S, '
    longitud = str(a[3] + (a[4] / 60) + (a[5] / 3600))[0:5] + '°W'
    aux = latitud + longitud
    line[4] = aux


def process_csv_data(reader_csv_data, writer):
    """Escribiendo nuevo contenido en orden específico,teniendo en cuenta irregularidades del data-set
    """
    encabezados = reader_csv_data.__next__()  # Escribo titulares separados por coma (cómo venían)..
    encabezados.append(encabezados.pop(0))
    writer.writerow(encabezados)

    for line in reader_csv_data:
        names = line.pop(0)
        line.append(names)
        evaluate_empty_fields(line)
        evaluate_coordinates(line)
        writer.writerow(line)


def evaluate_empty_fields(line):
    if '' == line[2]:  # Posición relativa a Profundidad Media (m)
        line[2] = 'Desconocido'
    if '' == line[3]:  # Posición relativa a Profundidad Máxima (m)
        line[3] = 'Desconocido'


def obtain_csv_dataset(csv_file):
    """Esta funcion recibe el dataset referente a lagos, y crea una copia con modificaciones solicitados en formato csv
    """
    path_new_file = route_new_file()

    with open(csv_file, 'r') as data_set, open(path_new_file, 'w') as new_csv:
        file_reader = csv.reader(data_set)
        writer = csv.writer(new_csv)
        process_csv_data(file_reader, writer)


def generate_csv():
    try:
        obtain_csv_dataset(route_csv_file_to_work())
    except FileExistsError as error:
        print(f'Existe el csv que desea generar, => {error.__str__()}')
    except FileNotFoundError as not_found_f:
        print(f'No se ha hallado un archivo existente, error:{not_found_f}')


if __name__ == "__main__":
    #generate_csv()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55")

    print(sys.path)
    print(os.path.abspath(os.path.join('..', 'Consultas')))

