# organizador de archivos hecho en python
# se importan las librerías necesarias
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


def get_download_folder() -> Path:
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


def categorize_file(file_path: Path) -> str:
    """Devuelve la categoría de un archivo basado en su extensión."""
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Otros"


def organize_files_by_category(download_folder: Path) -> None:
    """Organiza los archivos en la carpeta especificada por categorías."""
    folders = {category: download_folder / category for category in CATEGORIES}
    for folder in folders.values():
        folder.mkdir(parents=True, exist_ok=True)
    for item in download_folder.iterdir():
        if item.is_file():
            category = categorize_file(item)
            shutil.move(str(item), str(folders[category] / item.name))


def main() -> None:
    download_folder = get_download_folder()
    print(f"Organizando archivos en la carpeta: {download_folder}")
    organize_files_by_category(download_folder)
    print("Organización completada.")


if __name__ == "__main__":
    main()


