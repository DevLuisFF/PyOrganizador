<h1 align="center">PyOrganizador</h1>

###

<p align="left">PyOrganizador es un script Python que organiza automáticamente los archivos descargados en carpetas según su extensión, manteniendo tu sistema ordenado y fácil de usar.</p>

###

<h2 align="left">Tecnologías:</h2>

###

<div align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.simpleicons.org/visualstudiocode/007ACC" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.simpleicons.org/git/F05032" height="40" alt="git logo"  />
</div>

###

<h2 align="left">Requisitos:</h2>

###

<p align="left">-Python 3.x<br>-Git</p>

###

<h2 align="left">Instalación:</h2>

###

<p align="left">-Clona o descarga este repositorio:<br><br>git clone https://github.com/DevLuisFF/PyOrganizador.git<br><br>-Navega al directorio del proyecto:<br><br>cd PyOrganizador</p>

###

<h2 align="left">Uso:</h2>

###

<p align="left">-Ejecuta el script manualmente:<br><br>python3 PyOrganizador.py<br><br>El script organizará los archivos en la carpeta de Descargas en subcarpetas según su tipo (Imágenes, Documentos, Programas, Videos, Música, Otros).</p>

###

<h2 align="left">Automatización:</h2>

###

<h4 align="left">En Windows:</h4>

###

<p align="left">-Abre el Programador de Tareas.<br>-Crea una Tarea Básica.<br>-En Nombre, pon algo como "Organizar Descargas".<br>-Configura el Desencadenador para que se ejecute cada 30 minutos.<br>-En Acción, selecciona Iniciar un programa.<br>-Selecciona python o la ruta a tu intérprete de Python, y como argumento pon la ruta completa a tu script PyOrganizador.py.</p>

###

<h4 align="left">En macOS y Linux:</h4>

###

<p align="left">-Abre una terminal.<br>-Edita el crontab usando crontab -e.<br><br>-Añade la siguiente línea al final del archivo (reemplaza /ruta/a/tu/script con la ruta real a tu script):<br><br>*/30 * * * * /usr/bin/python3 /ruta/al/script/organizador_descargas.py<br><br>-Esto configurará cron para ejecutar el script cada 30 minutos.</p>

###

<h2 align="left">Notas:</h2>

###

<p align="left">-Si el script no puede encontrar automáticamente la carpeta de Descargas, te pedirá que ingreses la ruta manualmente.<br>-Las categorías y sus extensiones asociadas se pueden modificar editando el diccionario CATEGORIES en el script.</p>

###

<h2 align="left">Contribución:</h2>

###

<p align="left">-Haz un fork del proyecto.<br>-Crea una nueva rama (git checkout -b feature-nueva-caracteristica).<br>-Realiza tus cambios y haz commit (git commit -am 'Añadir nueva característica').<br>-Haz push a la rama (git push origin feature-nueva-caracteristica).<br>-Crea un nuevo Pull Request.</p>

###
