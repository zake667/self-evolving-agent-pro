import os

def read_file(path):
    """
    Lee el contenido de un archivo de forma segura.

    Args:
        path (str): Ruta al archivo que se desea leer.

    Returns:
        str: El contenido del archivo o un mensaje de error si no se encuentra.
    """
    if not os.path.exists(path):
        return f"Error: File {path} not found."
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    """
    Escribe contenido en un archivo, creando los directorios padre si no existen.

    Args:
        path (str): Ruta donde se guardará el archivo.
        content (str): Texto a escribir en el archivo.

    Returns:
        str: Mensaje confirmando el éxito de la operación.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File {path} written successfully."
