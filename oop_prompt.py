#Object Oriented Prompt

class Podracer:
  def __init__(self, in_max_speed,in_condition, in_price):
    self.max_speed = in_max_speed
    self.condition = in_condition
    self.price = in_price

  def repair(self):
    self.condition ="repaired"
    print(f"The Podracer has been repaired")

class Anakinspod(Podracer):
  def __init__(self,in_max_speed,in_condition,in_price):
     super().__init__(in_max_speed,in_condition, in_price)
      
  def boost(self):
     self.max_speed *= 2
     print(f"Boost engaged: New Max Speed of {self.max_speed}") 

class Sebulbaspod(Podracer):
  def __init__(self,in_max_speed,in_condition,in_price):
     super().__init__(in_max_speed,in_condition, in_price)
      
  def flame(self,in_podracer):
     in_podracer.condition = "trashed"
     print(f"The podracer has been flamed and trashed by Sebulba")
    
podracer_1= Podracer(180,"trashed",199)
podracer_1.repair()
podracer_2 = Podracer(170,"new",599)

anakin_podracer = Anakinspod(200,"New",599)
anakin_podracer.boost()
sebulbas_podracer = Sebulbaspod(190,"New",599)
sebulbas_podracer.flame(podracer_2)
print(podracer_2.condition)

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation -  by creating a class we are combing data attributes and methods directly related to the object class
# Abstraction - we are only providing the methods(dashboard) to the user they can use without having to provide them on how the code(engine) works. 
# Inheritance - by creating a child class , the new child classes have access to the attributes and methods of the parent class
# Polymorphism - we are able to extend or expand the parent class and only specific for that child class

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    ## Not in this situation because we are in need of changing the state of instance values

# How in particular did Object Oriented Programming assist in the solving of this problem?
    ## By using OOP it allows us to group attributes and methods with their respective class.