import json
def get_path_actual(nombre_archivo):
    """_summary_
        Consigue el directorio actual

    Args:
        nombre_archivo (str): el  nombre del archivo 

    Returns:
        path: retorna una instancia de la clase os que tiene el atributo "path" que es un string y lo une al nombre del archivo con el metodo join que tienen los str
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def archivo_a_lista(archivo_csv):
    """_summary_
        toma un archivo_csv y convierte en una lista de diccionarios
    

    Args:
        archivo_csv (str): el nombre del archivo

    Returns:
        list: una lista de diccionarios
    """
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lista = []
        archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            jugador = {}
            linea = linea.strip("\n").split(",")
            nombre,puntaje, tiempo, cantidad_enemigos = linea
            
            
            jugador["nombre"] = nombre
            jugador["puntaje"] = puntaje
            jugador["tiempo"] = tiempo
            jugador["cantidad_enemigos"] = cantidad_enemigos
            lista.append(jugador)
        
        
    return lista

def json_a_lista(ruta_archivo):
    """
    Lee un archivo JSON y lo convierte en una lista de diccionarios.

    
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lista_diccionarios = json.load(archivo)
        return lista_diccionarios
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
    except json.JSONDecodeError:
        print(f"El archivo {ruta_archivo} no contiene un JSON válido.")
    return []

def guardar_csv(lista: list, nombre_archivo: str):
    """
    Guarda los elementos de la lista en un archivo .csv.

    Args:
        lista (list): Lista de diccionarios.
        nombre_archivo (str): Nombre del archivo.
    """
    if not lista:
        return  
    
    # Obtener las claves del primer diccionario para el encabezado
    encabezado = list(lista[0].keys())
    
    # Abrir el archivo en modo de escritura
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        # Escribir el encabezado
        archivo.write(",".join(encabezado) + "\n")
        
        # Escribir las filas
        for elemento in lista:
            linea = ",".join(str(elemento[key]) for key in encabezado)
            archivo.write(linea + "\n")
            
def guardar_json(lista: list, nombre_archivo: str):
    
    """Guarda una lista de diccionarios en un archivo .json
    """
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        
        json.dump(lista, archivo, ensure_ascii=False, indent=4)

