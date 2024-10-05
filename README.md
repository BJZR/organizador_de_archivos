# Organizador de Archivos

Este script en Python permite organizar automáticamente los archivos en un directorio dado según su tipo, moviéndolos a carpetas específicas basadas en sus extensiones. Además, soporta la descompresión automática de archivos comprimidos como `.zip` y `.tar`. Es una herramienta útil para mantener el orden en directorios con una gran cantidad de archivos.

## Características

- **Organización por tipo de archivo**: Clasifica automáticamente los archivos en carpetas como `imagenes`, `videos`, `documentos`, `audio`, etc., basándose en su extensión.
- **Soporte para formatos comunes**: Soporta una amplia variedad de formatos, incluyendo imágenes (`.jpg`, `.png`), videos (`.mp4`, `.avi`), documentos (`.pdf`, `.docx`), audio (`.mp3`, `.wav`), archivos comprimidos (`.zip`, `.tar`), entre otros.
- **Descompresión automática**: Descomprime archivos `.zip` y `.tar` en sus respectivas carpetas automáticamente.
- **Manejo de duplicados**: Si un archivo con el mismo nombre ya existe en la carpeta destino, el script renombra el archivo duplicado para evitar sobrescribir.
- **Eliminación de carpetas vacías**: Las carpetas vacías creadas durante la organización son eliminadas automáticamente para mantener limpio el directorio.

## Requisitos

- Python 3.x
- No se requieren librerías externas, ya que utiliza módulos estándar de Python como `os`, `shutil`, `zipfile`, y `tarfile`.

## Instalación

1. Clona este repositorio o descarga el script directamente.
2. Asegúrate de tener Python 3 instalado en tu sistema.

```bash
git clone https://github.com/tu-repositorio/organizador-archivos.git
cd organizador-archivos
