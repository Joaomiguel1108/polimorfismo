class Cachorro:

  def move(self):
    print("au au!")

class gato:
  

  def move(self):
    print("miau!")


car1 = Cachorro()       
boat1 = gato() 


for x in (car1, boat1):
  x.move()
  
