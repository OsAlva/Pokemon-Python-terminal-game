class Pokemon:
  def __init__(self, name, type, level = 5):
    self.name = name
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.type = type
    self.is_knocked_out = False

## Imprimir un pokemon le dirá su nombre, su tipo, su nivel y cuánta salud le queda
  def __repr__(self):
    return  "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level = self.level, name = self.name, health=self.health, type = self.type)

  def revive(self):
#si revivimos un pokemon cambiamos el status a false
    self.is_knocked_out = False
 # Un pokemon revivido no puede tener 0 de salud. revive() solo se llama si el pokemon recibio algo de salud, pero si de alguna manera no tiene salud su salud se establece a 1.
    if self.health == 0:
        self.health = 1
    print("{name} was revived!!".format(name = self.name))

  def knock_out(self):
## Noquear a un pokemon cambiará su estado a True.
    self.is_knocked_out = True
#Un pokemon noqueado no puede tener salud. knock_out() solo debe llamarse si la salud se estableció en 0, pero si de alguna manera al Pokémon le quedaba salud, se establece en 0.
    if self.health != 0:
      self.health = 0
    print("{name} was knocked out!".format(name=self.name))

  def lose_health(self,amount):
## Reduce la salud de un pokemon e imprime la salud restante actual
    self.health -= amount
    if self.health <=0:
# Asegurate que la salud no se vuelva negativa, antes de eso noquea al pokemon.
      self.health = 0
      self.knock_out()
    else:
      print("{name} now has {health} health.".format(name=self.name, health=self.health))
  
  def gain_health(self,amount):
#Agrega health a un pokemon, si un pokemon pasa de 0 salud, entonces revivelo.
    if self.health == 0:
      self.revive()
    self.health += amount
#Se asegura de que la salud no supere la salud maxima
    if self.health >= self.max_health:
      self.health = self.max_health
    print("{name} now has {health} health.".format(name = self.name, health = self.health))

  def attack(self, other_pokemon):
# nos aseguramos que el pokemon no esta knocked out
    if self.is_knocked_out:
      print("{name} can't attack beacuse it is knocked out!".format(name = self.name))
      return
    if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
      print("It's not very effective")
      other_pokemon.lose_health(round(self.level * 0.5))
# Si el pokemon que ataca no tiene ni ventaja ni desventaja, entonces hace daño igual a su nivel al otro pokemon
    if (self.type == other_pokemon.type):
      print("{my_name} attacked {other_name} for {damage} damage".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
      other_pokemon.lose_health(self.level)
#Si el pokemon atacante tiene ventaja, inflige daño igual al doble de su nivel al otro pokemon
    if(self.type =="Fire" and other_pokemon_type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
      print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
      print("It's supper effective")
      other_pokemon.lose_health(self.level * 2)


class Trainer:
  def __init__(self, pokemon_list, num_potions, name):
    self.pokemons = pokemon_list
    self.potions = num_potions
    self.current_pokemon = 0
    self.name = name

  def __repr__(self):
# Imprime el nombre del entrenador, los pokemons que tienen actualmente, y el pokemon activo actual.
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

  def switch_active_pokemon(self,new_active):
#Cambia el pokemon activo al numero dado como parametro, primero verifica que el numero sea valido(entre 0 y la longitud de la lista)
    if new_active < len(self.pokemons) and new_active >= 0:
#No puedes cambiar a un pokemon que este noqueado
      if self.pokemons[new_active].is_knocked_out:
        print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
#No puedes cambiar a tu pokemon actual
      elif new_active == self.current_pokemon:
        print("{name} is already your active pokemon".format(name=self.pokemons[new_active].name))
#Cambia pokemon
      else:
        self.current_pokemon = new_active
        print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

  def use_potion(self):
  #usamos posion en un pokemon, tenemos que tener almenos una pocion.
    if self.potions > 0:
      print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
#Una pocion recupera 20 de vida
      self.pokemons[self.current_pokemon].gain_health(20)
      self.potions -= 1
    else:
      print("You don't have any more potions")

def attack_other_trainer(self, other_trainer):
# Tu pokemon actual ataca al pokemon actual del otro entrenador
  my_pokemon = self.pokemons[self.current_pokemon]
  their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
  my_pokemon.attack(their_pokemon)

#Seis pokemons son dado con diferentes niveles. Si no se da ningún nivel, es el nivel 5

a=Pokemon("Charmander", "Fire",7)
b=Pokemon("Squirtle","Water")
c=Pokemon("Lapras","Water",9)
d=Pokemon("Bulbasaur","Grass",10)
e=Pokemon("Vulpix","Fire")
f=Pokemon("Staryu","Water",4)

#obtener informacion de los entrenadores y seleccionar pokemons
trainer_one_name = input("Welcome to the world of Pokemon. Please enter a name for player one and hit enter.")
trainer_two_name = input("Hi, "+ str(trainer_one_name) + "! Welcome! Let's find you an opponent. Enter a name for the second player.")

choice = input("Hi, " + trainer_two_name + "! Let's pick our Pokemon! " + trainer_one_name + ", would you like a Level 7 Charmander, or a Level 7 Squirtle? " + trainer_two_name + " will get the other one. Type either 'Charmander' or 'Squirtle'. ")

while choice != 'Charmander' and choice != 'Squirtle':
  choice = input("Whoops, it looks like you didn't choose 'Charmander' or 'Squirtle'. Try selecting one again!")

## Hacer un seguimiento de qué pokemon eligieron
trainer_one_pokemon = []
trainer_two_pokemon = []

if choice == 'Charmander':
  trainer_one_pokemon.append(a)
  trainer_two_pokemon.append(b)
else:
  trainer_one_pokemon.append(b)
  trainer_two_pokemon.append(a)

#Seleccionamos el segundo pokemon
choice = input(trainer_two_name + ", would you like a Level 9 Lapras, or a Level 10 Bulbasaur? " + trainer_one_name + " will get the other one. Type either 'Lapras' or 'Bulbasaur'. ")

while choice != 'Lapras' and choice != 'Bulbasaur':
  choice = input("Whoops, it looks like you didn't choose 'Lapras' or 'Bulbasaur'. Try selecting one again! ")

if choice == 'Lapras':
  trainer_one_pokemon.append(d)
  trainer_two_pokemon.append(c)
else:
  trainer_one_pokemon.append(c)
  trainer_two_pokemon.append(d)

#Seleccionamos el tercer pokemon
choice = input(trainer_one_name + ", would you like a Level 5 Vulpix, or a Level 4 Staryu? " + trainer_two_name + " will get the other one. Type either ' Vulpix' or 'Staryu'. ")

while choice != 'Vulpix' and choice != 'Staryu':
  choice = input("Whoops, it looks like you didn't choose 'Vulpix' or 'Staryu'. Try selecting one again! ")

if choice == 'Vulpix':
  trainer_one_pokemon.append(e)
  trainer_two_pokemon.append(f)
else:
  trainer_one_pokemon.append(f)
  trainer_two_pokemon.append(e)

#Creando los objetos Entrenador con los nombres dados y las listas de pokemon
trainer_one = Trainer(trainer_one_pokemon, 3, trainer_one_name)
trainer_two = Trainer(trainer_two_pokemon, 3, trainer_two_name)

print(trainer_one)
print(trainer_two)

## Probando ataques, dando pociones y cambiando pokemon. Esto podría desarrollarse más para solicitar información
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)
  








