import os
import shutil
import zipfile
import tarfile

# Función para organizar los archivos
def organizar_archivos(directorio):
    # Diccionario de configuración para mapear extensiones de archivo a carpetas de destino
    configuracion = {
        ".jpg": "imagenes",
        ".jpeg": "imagenes",
        ".png": "imagenes",
        ".gif": "imagenes",
        ".bmp": "imagenes",
        ".tiff": "imagenes",
        ".mp4": "videos",
        ".avi": "videos",
        ".mkv": "videos",
        ".mp3": "audio",
        ".wav": "audio",
        ".flac": "audio",
        ".ogg": "audio",
        ".doc": "documentos_office",
        ".docx": "documentos_office",
        ".ppt": "documentos_office",
        ".pptx": "documentos_office",
        ".xls": "documentos_office",
        ".xlsx": "documentos_office",
        ".pdf": "documentos",
        ".txt": "documentos",
        ".zip": "archivos_comprimidos",
        ".rar": "archivos_comprimidos",
        ".7z": "archivos_comprimidos",
        ".tar": "archivos_comprimidos",
        ".gz": "archivos_comprimidos",
        ".exe": "ejecutables",
        ".msi": "ejecutables",
        ".apk": "aplicaciones",
        ".nes": "juegos",
        ".gba": "juegos",
        # Agrega más extensiones según tus necesidades
    }

    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Diccionario para rastrear qué carpetas están vacías
    carpetas_vacias = {}

    # Iterar sobre cada archivo
    for archivo in archivos:
        ruta_completa = os.path.join(directorio, archivo)

        # Ignorar carpetas y archivos ocultos
        if not archivo.startswith('.') and os.path.isfile(ruta_completa):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()  # Convertir la extensión a minúsculas

            # Determinar la carpeta de destino
            carpeta_destino = configuracion.get(extension, "otros")

            # Directorio de destino
            directorio_destino = os.path.join(directorio, carpeta_destino)

            # Crear el directorio de destino si no existe
            if not os.path.exists(directorio_destino):
                os.makedirs(directorio_destino)
                print(f"Creando carpeta: {carpeta_destino}")

            # Verificar si el archivo ya existe en la carpeta destino
            destino_archivo = os.path.join(directorio_destino, archivo)
            if os.path.exists(destino_archivo):
                nombre, ext = os.path.splitext(archivo)
                contador = 1
                nuevo_nombre = f"{nombre}_{contador}{ext}"
                destino_archivo = os.path.join(directorio_destino, nuevo_nombre)

                # Seguir generando nombres únicos si ya existe un duplicado
                while os.path.exists(destino_archivo):
                    contador += 1
                    nuevo_nombre = f"{nombre}_{contador}{ext}"
                    destino_archivo = os.path.join(directorio_destino, nuevo_nombre)

                print(f"Archivo duplicado renombrado a: {nuevo_nombre}")

            # Mover el archivo al directorio de destino
            shutil.move(ruta_completa, destino_archivo)
            print(f"Moviendo: {archivo} -> {carpeta_destino}")

            # Marcar la carpeta como no vacía
            carpetas_vacias[carpeta_destino] = True

            # Si es un archivo comprimido, descomprimirlo
            if carpeta_destino == "archivos_comprimidos":
                descomprimir_archivo(destino_archivo, directorio_destino)

    # Eliminar carpetas vacías
    for carpeta in os.listdir(directorio):
        carpeta_ruta = os.path.join(directorio, carpeta)
        if os.path.isdir(carpeta_ruta) and not os.listdir(carpeta_ruta):
            os.rmdir(carpeta_ruta)
            print(f"Eliminando carpeta vacía: {carpeta}")

# Función para descomprimir archivos ZIP o TAR
def descomprimir_archivo(ruta_archivo, directorio_destino):
    try:
        if zipfile.is_zipfile(ruta_archivo):
            with zipfile.ZipFile(ruta_archivo, 'r') as zip_ref:
                zip_ref.extractall(directorio_destino)
                print(f"Descomprimiendo archivo ZIP: {ruta_archivo}")
        elif tarfile.is_tarfile(ruta_archivo):
            with tarfile.open(ruta_archivo, 'r') as tar_ref:
                tar_ref.extractall(directorio_destino)
                print(f"Descomprimiendo archivo TAR: {ruta_archivo}")
        # Se pueden agregar más formatos de archivo comprimido aquí
    except Exception as e:
        print(f"Error al descomprimir {ruta_archivo}: {e}")

# Solicitar al usuario la ruta del directorio a organizar
directorio_origen = input("Ingrese la ruta del directorio a organizar: ")

# Verificar si la ruta proporcionada es válida
if os.path.isdir(directorio_origen):
    # Llamar a la función para organizar los archivos en el directorio de origen
    organizar_archivos(directorio_origen)
    print("Archivos organizados correctamente.")
else:
    print("La ruta proporcionada no es válida.")
