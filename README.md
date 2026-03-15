# Catálogo
## Programa
### Diagrama de clases
### Herencia
### Gestión de recursos
### Resultado
## Sitio Web
Ahora que hemos diseñado nuestro código, lo convertiremos en una página web, para ello necesitamos:
* Una cuenta en GIthub.
  
  https://github.com/
  
* Una cuenta en Render.
  
  https://render.com/
  
* Tener instalado Gitbash en tu equipo.

1️⃣**Estructura**

Crea una carpeta que contendra:
* main.py
* Carpeta de imagenes para el catálogo.
* requirements.txt

El archivo de texto *requirements*, debe contener la palabra **flet**.

2️⃣**Gitbash**

Abre Gitbash dentro del entorno virtuarl flet, escribe lo siguinete en Gitbash para activar el entorno flet.
  ```bash
  source .venv/Scripts/activate
  ```
Ahora, ingresa a la carpeta de tu proyecto y configura tu nombre y correo, estos deben ser los mismo que en GitHub.
  ```bash
 git config --global user.name "Tu Nombre"
  ```
  ```bash
 git config --global user.email "tuemail@gmail.com"
  ```
Convierte tu carpeta en un repositorio con:
  ```bash
  git init
  ```
Agrega todos los archivos del proyecto.
  ```bash
  git add .
  ```
Crea tu primer *commit*, para especificar que cambios se hicieron en el proyecto.
  ```bash
  git commit -m "Primer commit "
  ```
  
3️⃣**Github**

Crea un nuevo repositorio, puedes poner el nombre que desees, pero es recomendable el nombre del proyecto que subiras, no crees un Readme, deja la configuración predeterminada de Github. 

4️⃣**Conección**

Una vez creado nuestro repositrio, volvemos a Gitbash e ingresamos:
 ```bash
  git remote add origin https://github.com/TU-USUARIO/nombree-repositorio.git
  ```
Para ligar el repositorio a Gitbash.

  ```bash
git branch -M main
git push -u origin main
  ```
Esto enviara tu proyeto a el repositorio de GitHub anteriormente seleccionado.

5️⃣**Crear la web en Render**

Creamos una nueva Web Service, la conectamos a nuestra cuenta de GitHub y seleccionamos el repositorio de nuestro proyecto.

En el área de **Build Command** escribe lo siguinete:
  ```bash
pip install -r requirements.txt
  ```
Y en **Start Command**
  ```bash
python main.py
  ```
Una vez específicado, damos click en el boton para inicializar el proceso.

Sí, todo sale bien te dara un link com el siguinete:

https://proyecto-catalogo-7p52.onrender.com

Esto quiere decir que tu catálogo ya es na página web.🥳
* Un punto importante es que al usar el sevicio gratuito de *Render*,la página puede tardar un poco en cargar.
### Resultado

