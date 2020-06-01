# dictionar with pokemon type advantages, first type in value is stronger than second in pair 
pokemon_advantages = { 'adv_1': ["Fire", "Grass"], 'adv_2':["Water", "Fire"], 'adv_3': ["Grass", "Water"]  }

class Pokemon():
  def __init__(self, name, level, p_type):
    self.name = name
    self.level = level
    self.p_type = p_type
    self.health = 100 * level
    self.max_health = 100 * level
    self.exp = 0
    self.max_exp = 5 * level
    self.knocked_down = False
    self.atk = 20
    self.deff = 10

  def __repr__(self):
    return self.name
    return self.p_type

  def knocked_out(self):
    self.knocked_down = True
    self.health = 0
    print("{name} is knocked down.".format(name = self.name))

  def lose_health(self, lose_health):
    self.health -= lose_health
    if self.health > 0:
      print("{name} lose health! Curent health brings: {health} points".format(name=self.name, health=self.health))
    else:
      self.knocked_out()
    
  def gain_health (self, add_health):
    self.health += add_health
    if self.knocked_down == True:
      self.health = 0
      print("{name} is KO!!! You should first revive Pokemon".format(name=self.name))
    elif self.health < self.max_health:
      print("{name} recovered +{h} health points, current have {health} health points".format(h = add_health, name=self.name, health=self.health))
    else:
      self.health = self.max_health
      print("{name} recovered MAX health points, current have {health} health points".format(name=self.name, health=self.health))
  
  def revive(self):
    if self.knocked_down == True:
      self.knocked_down = False
      self.health = 100
      print ("{name} is revive!!!".format(name = self.name))
      print ("{name} current health points: {health}".format(name = self.name, health = self.health))
    else: 
      print("{p} is still alive.".format(p = self.name))
      
  def attack(self, other_p):
    ind = self.atk - other_p.deff
    if self.knocked_down == True or other_p.knocked_down == True:
      print("One of Pokemon's are KO, attack is not possible.")
    else:
      damage = (self.level*ind)
      for p1,p2 in pokemon_advantages.values():
        if self.p_type == p1 and other_p.p_type == p2:
          damage = 2 * self.level * ind
          self.atk+=1
          other_p.deff+=2
          break         
        else:
          continue
      print( self.name+" attack " + other_p.name +" for "+str(damage))
      other_p.lose_health(damage)
      if damage == self.level*ind:
        self.atk+=2
        other_p.deff+=1
      else:
        pass
      self.exp_up()
    
  def exp_up(self):
    self.exp+=1
    if self.exp < self.max_exp:
      print("{name} receive new exp points. Total exp points is {exp}.".format(name=self.name, exp=self.exp))
    else:
      self.exp = 0
      self.level+= 1
      self.max_exp = self.level*5
      self.health = self.level*100
      self.max_health = self.level*100
      print("Congratulations {name} level up!!!. New level is {lvl}.".format(name=self.name, lvl=self.level))

  def stats(self):# display actual stats pokemons 
    print("Name: {n}\n Type: {t}\n Level: {l}\n Health|max: {h}|{hm}\n Exp|max: {e}|{em}\n Attack: {a}\n Defence: {d}\n".format(n=self.name,t=self.p_type,l=self.level, h=self.health, hm=self.max_health, e=str(self.exp), em=str(self.max_exp), a=self.atk, d=self.deff))
    

class Trainer(): 
  def __init__(self, name, pokemons, current_pokemon = "N/A"):
    self.name = name
    self.pokemons = pokemons
    self.potions = int(len(pokemons))
    self.current_pokemon = current_pokemon
    
  def __repr__(self):
    return self.name

  def potion(self):
    try:
      pots = int(input("How many potions do you want use?:"))
      pot = int(pots)
      if pot <=0:
        print("You don't have any potion.")
      elif self.potions >= pot:
        pokemon = self.current_pokemon
        if pokemon != "N/A":
          if pokemon.health == pokemon.max_health:
            pokemon.gain_health(50)
          else:
            self.potions -= pot
            pokemon.gain_health(50*pot)
        else:
          print("Pick pokemon!")
      else:
        print("You don't have enough potions.")
    except ValueError:
        print("Put in only value.")
 
  def pick_p(self):# set a current pokemon,
    print ("Available pokemons to set a active pokemon: "+ str(self.pokemons))
    pokemon_in = input("Your choice?:")
    pokemon = pokemon_in.title()
    for i in range(0, len(self.pokemons)):
      if pokemon == self.pokemons[i].name:
        if self.pokemons[i].knocked_down == False:
          self.current_pokemon = self.pokemons[i]
          print ("{p} is active pokemon".format(p = pokemon))
          break
        else:
          print("You can't pick this pokemon, {p} is KO.".format(p = pokemon ))
          break
      else:
        if i < len(self.pokemons)-1:
          continue
        else:
          print("You can't pick this pokemon, {p} is not available for You.".format(p= pokemon))

  def attack_other_trainer(self): # attack between current pokemons, belonging to two different trainers
    print("Available trainers to attack:")
    print(trainers_to_attack)
    other = input("Pick trainer to attack: ")
    other_trainer = other.title()
    for i in range(0, len(trainers_to_attack)):
      if self.name == other_trainer:
        print("You can't attack self!")
        break
      elif other_trainer == trainers_to_attack[i].name:
        if self.current_pokemon != "N/A" and trainers_to_attack[i].current_pokemon!= "N/A" :
          print("{t1} pick {p1} and attack {t2} who pick to defence a {p2}".format(t1 = self.name, p1 = self.current_pokemon.name, t2 = trainers_to_attack[i].name, p2 = trainers_to_attack[i].current_pokemon.name))
          self.current_pokemon.attack(trainers_to_attack[i].current_pokemon)
          break
        else:
          if self.current_pokemon == "N/A" and trainers_to_attack[i].current_pokemon == "N/A":
            print ("{t1} and {t2} should pick pokemons to fight.".format(t1 = self.name, t2 = trainers_to_attack[i].name))
            break
          elif self.current_pokemon == "N/A":
            print ("{t1} should pick pokemon to fight.".format(t1 = self.name))
            break
          else:
            print ("{t1} should pick pokemon to fight.".format(t1 = trainers_to_attack[i].name))
            break
      else:
        if i < len(trainers_to_attack)-1:
          continue
        else:
          print(other_trainer + " didn't exist. Pick trainer from above list.")

  def add_p(self): # add new pokemon to trainer pocket with available pokemons
    print ("Available pokemons to add your pocket, "+ self.name+":")
    print(available_pokemons)
    pokemon_in = input("Which pokemon you want to add to your pocket?:")
    new_p = pokemon_in.title()
    for i in range(0, len(available_pokemons)):
      if new_p == available_pokemons[i].name:
        if not available_pokemons[i] in self.pokemons:
          self.pokemons.append(available_pokemons[i])
          print("{np} is added to Your pocket.".format(np = new_p))
          print("Current pocket:")
          print(self.pokemons)
          break
        else:
          print("You had {np} in pocket before.".format( np = new_p))
          break
      else:
        if i < len(available_pokemons)-1:
          continue
        else:
          print("Pokemon didn't exist.")

  

# Test it :) 
a = Pokemon("Pokemon 1", 1, "Fire")
b = Pokemon("Pokemon 2", 1,"Grass")
c = Pokemon("Pokemon 3", 1,"Water")
d = Pokemon("Pokemon 4", 1,"Water")
t1 = Trainer("Trainer 1", [a,b,c,d],a)
t2 = Trainer("Trainer 2", [a,b,d],b)
t3 = Trainer("Trainer 3",[a,d])
t4 = Trainer("Trainer 4",[a])
trainers_to_attack = [t1,t2,t3,t4]
available_pokemons = [a,b,c,d]


