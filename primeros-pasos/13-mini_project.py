# Registro
# Recibas de forma dinámica nombre, año de nacimiento, correo y contraseña


"""
  Nombre: Ricado 
  Email: omarhrn@gmail.com
  Tendrás 55 años en el 2050
  Tu contraseña es: ****
"""

nombre = input("Nombre: ")
email = input("Email: ")
year_of_birth = input("Año de nacimiento: ")
password = input("Contraseña: ")

age = 2025 - int(year_of_birth)
password = len(password)

message = f'''
  Nombre: {nombre}
  Email: {email}
  Tendrás {age} años en el 2050
  Tu contraseña es: {'*' * password}
'''
print(message)