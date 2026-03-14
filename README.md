# Sistema de Registro de Productos

## Descripción

Este proyecto es un programa simple desarrollado en **Python** que permite registrar productos desde la terminal.

El usuario puede ingresar los siguientes datos:

- Nombre del producto
- Precio unitario
- Cantidad

El programa calcula automáticamente el **costo total** multiplicando el precio por la cantidad y muestra la información en pantalla.

Además, el repositorio incluye un **diagrama de flujo en formato PDF** que representa la lógica del programa.

---

## Requisitos

Para ejecutar este programa necesitas tener instalado:

- **Python 3**

Puedes verificar si Python está instalado ejecutando el siguiente comando en la terminal:


python --version


Si Python está instalado, el sistema mostrará la versión instalada.

---

# Cómo clonar el repositorio

Este proyecto se encuentra en la rama **H1** del repositorio.

Para clonar el repositorio ejecuta el siguiente comando:


git clone https://github.com/Dan623280/Historia-de-Usuario.git


Luego entra a la carpeta del proyecto:


cd Historia-de-Usuario


---

# Cómo traer la rama H1

Después de clonar el repositorio, debes cambiarte a la rama **H1** donde se encuentra el proyecto.

Primero descarga las ramas del repositorio:


git fetch


Luego cambia a la rama **H1**:


git checkout H1


Puedes verificar que estás en la rama correcta con:


git branch


La terminal mostrará algo similar a:


H1
main


El asterisco (*) indica la rama en la que te encuentras.

---

# Cómo ejecutar el programa

Una vez dentro de la carpeta del proyecto y ubicado en la rama **H1**, ejecuta el siguiente comando:


python inventario.py


El programa mostrará un mensaje de bienvenida y solicitará al usuario ingresar los datos del producto.

---

# Cómo utilizar el programa

El programa solicitará los siguientes datos:

1. Nombre del producto  
2. Precio unitario  
3. Cantidad del producto  

Después de ingresar los datos, el sistema mostrará la información del producto y el costo total.

Ejemplo de ejecución:


Nombre del producto: Lapiz
Precio Unitario del producto: 500
Cantidad: 3
Total: 1500


---

# Manejo de errores

El programa incluye validación de datos para evitar errores.

- Si el usuario introduce un valor inválido en el **precio**, el sistema mostrará un mensaje de error.
- Si el usuario introduce un valor inválido en la **cantidad**, el programa solicitará nuevamente el dato.

Esto garantiza que los cálculos se realicen correctamente.

---

# Diagrama de flujo del programa

El repositorio incluye un archivo con el diagrama de flujo del sistema:


M1S1.drawio.pdf


## Cómo abrir el archivo PDF

1. Descarga el archivo desde el repositorio.
2. Haz doble clic en el archivo **M1S1.drawio.pdf**.
3. El archivo se abrirá con cualquier lector de PDF como:

- Adobe Acrobat Reader
- Google Chrome
- Microsoft Edge
- Cualquier visor de PDF del sistema operativo

Este diagrama muestra las tres fases del programa:

- Entrada de datos
- Procesamiento
- Salida de resultados

---

# Estructura del proyecto


Historia-de-Usuario
│
├── inventario.py
├── README.md
└── M1S1.drawio.pdf


**inventario.py** → Programa principal del sistema  
**README.md** → Documentación del proyecto  
**M1S1.drawio.pdf** → Diagrama de flujo del programa

---

# Autor

**Daniel Elias Alvarez Diaz**