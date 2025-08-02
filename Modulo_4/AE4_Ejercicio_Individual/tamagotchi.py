class Tamagotchi:

   def __init__(self,nombre, color):

      self._nombre = nombre
      self._color = color
      self.salud_maxima = 100
      self.salud_actual = 100
      self.felicidad = 50
      self.energia = 100

   #Métodos:

   def jugar(self):

      if self.energia == 0:
         print("¡Tu tamagotchi se ha quedado sin energia!")
         pass
      else:
         print("La felicidad de tu tamagotchi aumentó en 10 😄")
         self.felicidad += 10
         if self.felicidad >= 100:
            print("¡Tu tamagotchi tiene su felicidad al máximo!")
            self.felicidad = 100

         print("La salud de tu tamagotchi disminuyó en 5! 🤒")
         self.salud_actual -= 5
         if self.salud_actual > self.salud_maxima:
            self.salud_actual = self.salud_maxima
            print("¡Tu tamagotchi está en perfecta salud!")
         print("La energia de tu tamagotchi disminuyó en 15! 😪")
         self.energia -= 15
         if self.energia < 0:
            self.energia = 0

   def comer(self):

      print("La felicidad de tu tamagotchi aumentó en 5! 😄")
      self.felicidad += 5
      print("La salud de tu tamagotchi aumentó en 5! 😄")
      self.salud_actual += 5
      if self.salud_actual > self.salud_maxima:
         self.salud_actual = self.salud_maxima
         print("Tu tamagotchi está en perfecta salud!")
      print("La energia de tu tamagotchi aumentó en 5! 😪")
      self.energia += 5
      if self.energia < 0:
         self.energia = 0

   def curar(self):

      print("La salud de tu tamagotchi aumentó en 20! 😄")
      self.salud_actual += 20
      print("La felicidad de tu tamagotchi disminuyó en 5! 😔")
      self.felicidad -= 5
      if self.felicidad < 0:
         self.felicidad = 0
   
   def dormir(self):

      print("La energia de tu tamagotchi aumentó en 60! 😄")
      self.energia += 60
      if self.energia > 100:
         self.energia = 100

   def golpear(self):

      print("ESO NO SE HACE! 😡")
      print("La salud de tu tamagotchi disminuyó en 40! 🤒")
      self.salud_actual -= 40
      if self.salud_actual < 0:
         self.salud_actual = 0
      print("La felicidad de tu tamagotchi disminuyó en 60! 😔")
      self.felicidad -= 60
      if self.felicidad < 0:
         self.felicidad = 0

   def mostrar_info(self):

      print(f"Nombre: {self._nombre}, Color: {self._color}")
      print("-" * 30)
      print(f"Salud: {self.salud_maxima}/{self.salud_actual}, Felicidad: {self.felicidad}, Energia: {self.energia}")

class Kuchipatchi(Tamagotchi):

   def __init__(self, nombre, color):

      super().__init__(nombre, color)
      self.salud_maxima += 20
      self.felicidad += 15

class Mimitchi(Tamagotchi):

   def __init__(self, nombre, color):

      super().__init__(nombre, color)
      self.salud_maxima += 20

class Pochitchi(Tamagotchi):

   def __init__(self, nombre, color):

      super().__init__(nombre, color)
      self.felicidad += 25