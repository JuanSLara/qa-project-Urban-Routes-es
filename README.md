**##Proyecto Sprint 8 – Automatización de Pruebas Urban Routes**

#Este proyecto fue desarrollado como parte del bootcamp de QA en **TripleTen**, grupo 31.
#Realizado por **Juan Lara**.

#Consiste en la automatización de pruebas de la aplicación **Urban Routes** usando **Python**,
# *Selenium WebDriver** y **Pytest**, bajo el patrón de diseño **Page Object Model (POM)*.


## 🛠 Tecnologías utilizadas

#- Python
#- Selenium WebDriver
#- Pytest
#- WebDriverWait (esperas explícitas, evitando time.sleep)
#- Page Object Model (POM)


## 📁 Estructura del proyecto
 #data.py = Datos de entrada: URL, telefonos, tarjetas, etc.
 #urban_routes_page.py = Clases y metodos base de la automatizacion
 #test_urban_routes.py = Contiene los 9 tests automatizados
 #retrieve_code.py = Codigo auxiliar proporcionado por el bootcamp
 #README.md = Descripcion del proyecto

## 📦Como ejecutar las pruebas
#1 Abre el proyecto en PyCharm
#2 Actualiza la URL en el archivo data/data.py con la direccion actual de la aplicacion a probar.
#3 Ejecuta las pruebas desde test_urban_routes.py

##Notas importantes
#Se utilizan esperas explicitas (WebDriverWait) para evitar problemas de sincronizacion.

##Autor
#Juan Lara
#Bootcamp de QA TripleTen
#Grupo 31
#2025
