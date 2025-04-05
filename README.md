# Prueba de Consumo de API - Reqres

Este proyecto en Python es una prueba práctica de cómo consumir una API REST utilizando el método **POST**, con validación de datos de entrada y manejo de respuestas. Se utiliza la API pública [Reqres](https://reqres.in/) para simular el registro de usuarios.

## 🚀 Características

- Captura de datos por consola (`nombre`, `apellido`, `email`, `contraseña`, `rol`)
- Validación de campos vacíos
- Validación de formato de correo y contraseña con expresiones regulares
- Envío de datos a la API mediante `requests.post()`
- Manejo de errores y respuestas de la API
- División lógica entre **registro de usuario** y **registro de acceso (login simulado)**

## 🧰 Tecnologías usadas

- Python 3
- Librería estándar `re` (expresiones regulares)
- Librería `requests`

## 📦 Instalación

1. Clona este repositorio o descarga el archivo `.py`.
2. Asegúrate de tener `requests` instalado.
3. Ejecuta el archivo.

##  Notas

-La API de Reqres es solo para pruebas, por lo tanto el registro real solo funciona con algunos emails predefinidos.
-Este script se enfoca en la lógica de validación y consumo de endpoints separados para usuario y autenticación.
-La contraseña debe tener al menos 6 caracteres y puede incluir letras, números y símbolos especiales (@#$%^&+=).

## Autor

Juan Camio Muñoz-Este proyecto fue desarrollado con fines educativos para reforzar el uso de APIs en Python.

## Licencia

Este codigo esta bajo una licencia MIT

