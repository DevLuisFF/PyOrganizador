# PyOrganizador

Este script en Python organiza automáticamente los archivos de la carpeta de Descargas en categorías como Imágenes, Documentos, Programas, Videos y Música. Es multiplataforma y puede configurarse para ejecutarse automáticamente cada 30 minutos.

## Requisitos

- Python 3.x

## Instalación

1. **Clona o descarga este repositorio:**

    
    git clone https://github.com/DevLuisFF/PyOrganizador.git
    

2. **Navega al directorio del proyecto:**

    
    cd PyOrganizador
    

## Uso

1. **Ejecuta el script manualmente:**

    
    python3 PyOrganizador.py
    

    El script organizará los archivos en la carpeta de Descargas en subcarpetas según su tipo (Imágenes, Documentos, Programas, Videos, Música, Otros).

## Automatización

### En Windows

1. Abre el **Programador de Tareas**.
2. Crea una **Tarea Básica**.
3. En **Nombre**, pon algo como "Organizar Descargas".
4. Configura el **Desencadenador** para que se ejecute cada 30 minutos.
5. En **Acción**, selecciona **Iniciar un programa**.
6. Selecciona `python` o la ruta a tu intérprete de Python, y como argumento pon la ruta completa a tu script `organizador_descargas.py`.

### En macOS y Linux

1. Abre una terminal.
2. Edita el crontab usando `crontab -e`.
3. Añade la siguiente línea al final del archivo (reemplaza `/ruta/a/tu/script` con la ruta real a tu script):

    
    */30 * * * * /usr/bin/python3 /ruta/a/tu/script/organizador_descargas.py
    

    Esto configurará `cron` para ejecutar el script cada 30 minutos.

## Notas

- Si el script no puede encontrar automáticamente la carpeta de Descargas, te pedirá que ingreses la ruta manualmente.
- Las categorías y sus extensiones asociadas se pueden modificar editando el diccionario `CATEGORIES` en el script.

## Contribución

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature-nueva-caracteristica`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
