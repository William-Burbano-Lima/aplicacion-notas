# notas.py
def mostrar_notas():
  try:
      with open("notas.txt", "r") as archivo:
          notas = archivo.readlines()
      print("Notas:")
      for nota in notas:
          print(nota.strip())
  except FileNotFoundError:
      print("No hay notas guardadas.")
      
      if __name__ == "__main__":
  agregar_nota("Esta es una nota de prueba.")
  mostrar_notas()