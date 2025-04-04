import requests  # Para hacer peticiones HTTP a la API
import re        # (Podrías usarlo para validar el email si quieres más adelante)

class PruebaReqres:
    def __init__(self):
        # Captura de datos del usuario desde la consola
        self.first_name = str(input("Ingresa tu nombre de usuario: ")).strip()
        self.last_name = str(input("Ingresa tus apellidos: ")).strip()
        self.job = str(input("Ingresa tu rol dentro de la empresa: ")).strip()
        self.email = str(input("Ingresa un correo electronico: ")).strip()
        self.password = str(input("Ingresa una contraseña: ")).strip()

        # Validación para asegurar que ningún campo esté en blanco
        if not all([self.first_name, self.last_name, self.job, self.email, self.password]):
            print("No se pueden ingresar campos en blanco.")
            return

        # URLs de la API de Reqres
        self.url_usuario = "https://reqres.in/api/users"     # Para simular creación de usuario
        self.url_registro = "https://reqres.in/api/register" # Para simular el registro con autenticación

    def subida_info(self):
        try:
            # Datos para la primera petición (crear usuario)
            data = {
                "first_name": f"{self.first_name}",
                "last_name": f"{self.last_name}",
                "job": f"{self.job}",
                "avatar": r"https://reqres.in/img/faces/1-image.jpg"  # Avatar de prueba
            }

            # Datos para la segunda petición (registro con email y contraseña)
            data_re = {
                "password": f"{self.password}",
                "email": f"{self.email}"
            }

            # Enviar los datos con método POST a las dos URLs
            respuesta_user = requests.post(self.url_usuario, json=data)
            respuesta_registro = requests.post(self.url_registro, json=data_re)

            # Validación del éxito de ambas peticiones
            if 200 <= respuesta_user.status_code < 300 and 200 <= respuesta_registro.status_code < 300:
                print("Registro subido con éxito.")
            else:
                print(f"Error en subida:\nUsuario: {respuesta_user.status_code}, {respuesta_user.text}\nRegistro: {respuesta_registro.status_code}, {respuesta_registro.text}")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")


# Punto de entrada del script
if __name__ == "__main__":
    info = PruebaReqres()
    info.subida_info()
