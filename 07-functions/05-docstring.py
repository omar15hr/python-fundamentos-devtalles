def hello(greet="hola", name="invitado"):
  """
  Info: Esta es una funciona para devolver un saludo personalizado
  """
  print(f"{greet}, {name}")


hello(name="Ricardo", greet="Hello")

def multiply(a: float, b: float) -> float:
  """
  Info: Multiplica dos numeros y devuelve el resultado
  """
  return a * b

print(multiply(2, 3))