from tamagotchi import Tamagotchi, Kuchipatchi, Mimitchi, Pochitchi
class Persona:

   def __init__(self, nombre, apellido, tamagotchi=None):

      self.__nombre = nombre
      self.__apellido = apellido
      self.__tamagotchi = tamagotchi

#Métodos

   def jugar_con_tamagotchi(self):
      
      print("Juegas con tu tamagotchi 😁")
      self.__tamagotchi.jugar()
      print("\n")

   def dar_comida(self):
      print("Alimentaste a tu tamagotchi 🍲")
      self.__tamagotchi.comer()
      print("\n")

   def curar_tamagotchi(self):
      print("Curaste a tu tamagotchi 💊")
      self.__tamagotchi.curar()
      print("\n")

   def dormir(self):
      print("😴😴😴")
      self.__tamagotchi.dormir()
      print("\n")

   def nono(self):
      self.__tamagotchi.golpear()
      print("\n")


   # Muestra la informacion del tamagotchi

   def mostrar_stats(self):
      self.__tamagotchi.mostrar_info()

   def mostrar_dueño(self):
      print(f"Dueño: {self.__nombre} {self.__apellido}")


   # Getters (se utilizó IA para apoyarse en esto)

   def get_nombre(self):
      return self.__nombre
   
   def get_apellido(self):
      return self.__apellido
   
   def get_tamagotchi(self):
      return self.__tamagotchi
   
   def get_nombre_completo(self):
      return f"{self.__nombre} {self.__apellido}"
   

   # Setter para asignar tamagotchi (se utilizó IA para apoyarse en esto)

   def set_tamagotchi(self, tamagotchi):
      if isinstance(tamagotchi, Tamagotchi):
         self.__tamagotchi = tamagotchi
      else:
         pass
