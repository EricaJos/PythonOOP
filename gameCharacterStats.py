#Create a class named GameCharacter that represents a game character and manages character stats.

#When instantiated, a new GameCharacter object should have the following attributes:

#_name set to the string given at the moment of the instantiation.
#_health set to 100
#_mana set to 50
#_level set to 1

class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

#Create a name property for read-only access to the character's name.
    @property
    def name(self):
        return self._name

#For the health property:
#Define a getter that returns the current health.
    @property
    def health(self):
        return self._health
#Define a setter that prevents health from being set below 0, and caps the health at 100.
    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        elif health > 100:
            self._health = 100
        else:
            self._health = health

#For the mana property:
#Define a getter that returns the current mana.
    @property
    def mana(self):
        return self._mana
#Define a setter that prevents mana from being set below 0, and caps the mana at 50.
    @mana.setter
    def mana(self, mana):
        if mana < 0:
            self._mana = 0
        elif mana > 50:
            self._mana = 50
        else:
            self._mana = mana

#Create a getter for level to return the character's current level.
    @property
    def level(self):
        return self._level
#Define a method named level_up that:
    def level_up(self):
#Increases the character's level by 1.
#Resets health to 100 and mana to 50 using their corresponding property setters.
#Prints a message in the form of <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
        self._level +=1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
        
#Define a __str__ method that returns a formatted string including:

#The character's name.
#The character's level.
#The character's current health.
#The character's current mana.