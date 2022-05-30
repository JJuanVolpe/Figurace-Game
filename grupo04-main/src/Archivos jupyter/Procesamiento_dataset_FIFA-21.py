# %%
import csv
import os

dir = os.path.realpath(".")
def abrir_archivo_y_obtener_datos():
    dir_entrada = os.path.join(dir,"Data sets/FIFA-21 Complete.csv")
    with open(dir_entrada,"r",encoding="utf8") as fifa_file:
        fifa_reader = csv.reader(fifa_file, delimiter=';')
        header, data_fifa = next(fifa_reader), list(fifa_reader)
    return header, data_fifa        

dir_salida = os.path.join(dir,"FIFA-21 Complete Modificado.csv")

def reemplazar_por_escala_conceptual(potential):
    if (int(potential) < 60):
        return "Regular"
    elif (60 <= int(potential) <= 79):
        return "Bueno"
    elif (80 <= int(potential) <= 89):
        return "Muy bueno"        
    else:
        return "Sobresaliente"

def reemplazar_por_posiciones_en_castellano(posicion):
    dicci_traducciones = {"GK":"Arquero", "SW":"Libero", "LB": "Lateral Izquierdo", "RB": "Lateral Derecho",
    "LWB":"Carrilero Izquierdo", "RWB":"Carrilero Derecho", "CB":"Defensor Central",
    "LCB":"Defensor Central Izquierdo", "RCB":"Defensor Central Derecho",
    "DM":"Mediocampista Defensivo", "CDM":"Mediocampista Defensivo Central", 
    "LDM":"Mediocampista Defensivo Izquierdo", "RDM":"Mediocampista Defensivo Derecho",
    "CM": "Mediocampista Central", "LCM":"Mediocampista Central Izquierdo",
    "RCM":"Mediocampista Central Derecho", "LM":"Mediocampista Izquierdo",
    "RM":"Mediocampista Derecho", "CAM":"Mediocampista Ofensivo Izquierdo",
    "LAM":"Mediocampista Ofensivo Derecho", "RAM":"Mediocampista Ofensivo Derecho",
    "SS": "Segundo Delantero", "LW":"Delantero Extremo Izquierdo",
    "RW":"Delantero Extremo Derecho", "CF":"Mediapunta", "ST":"Delantero Central",
    "LS":"Delantero Central Izquierdo", "RS":"Delantero Central Derecho" 
    } 
    posiciones = posicion.split("|")
    posiciones = [dicci_traducciones[pos] for pos in posiciones]
    return "|".join(posiciones)

def procesar_archivo(data):
    for row in data:
        row[7] = reemplazar_por_escala_conceptual(row[7])
        row[3] = reemplazar_por_posiciones_en_castellano(row[3])
    return data    

def generar_archivo(data_modificada):
    dir_salida = os.path.join(dir,"FIFA-21 Complete Modificado.csv")
    with open(dir_salida,"w",encoding="utf8") as present_file:    
        present_writer = csv.writer(present_file, delimiter=';')
        present_writer.writerow(["Team", "Nationality", "Position", "Age", "Potential", "Name"])
        [present_writer.writerow(row[8], row[2], row[3], row[5], row[7], row[1]) for row in data_modificada]

header, data = abrir_archivo_y_obtener_datos()        
data_modificada = procesar_archivo(data)    
generar_archivo(data_modificada)





