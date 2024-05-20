# organizador de archivos hecho en python
# se importan las librerias necesarias
import os
import shutil
import time
import sys
from pathlib import Path

# Diccionario de categorías y extensiones asociadas
CATEGORIES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Programas": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Música": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"],
}


def get_download_folder():
    """Intenta obtener la carpeta de descargas según el sistema operativo. Si falla, pide al usuario la ruta."""
    if sys.platform == "win32":
        download_folder = Path(os.path.join(os.getenv("USERPROFILE"), "Downloads"))
    elif sys.platform == "darwin":
        download_folder = Path(os.path.join(os.getenv("HOME"), "Downloads"))
    else:
        download_folder = Path(os.path.join(os.getenv("HOME"), "Descargas"))

    if not download_folder.exists():
        download_folder = Path(
            input(
                "No se pudo encontrar la carpeta de Descargas. Por favor, ingrese la ruta manualmente: "
            )
        )

    return download_folder


def categorize_file(file_path):
    """Devuelve la categoría de un archivo basado en su extensión."""
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Otros"


def organize_files_by_category(folder):
    """Organiza archivos en la carpeta especificada por categorías."""
    for item in folder.iterdir():
        if item.is_file():
            category = categorize_file(item)
            destination_folder = folder / category
            if not destination_folder.exists():
                destination_folder.mkdir()
            shutil.move(str(item), str(destination_folder / item.name))


def main():
    download_folder = get_download_folder()
    print(f"Organizando archivos en la carpeta: {download_folder}")
    organize_files_by_category(download_folder)
    print("Organización completada.")


if __name__ == "__main__":
    main()
