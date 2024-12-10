class animal:
  def __init__(self, cor):
    self.cor = cor

  def falar(self):
    pass

class peixe(animal):
    def falar(self):
        print("peixes nao falam")
class Cachorro(animal):
    def falar(self):
        print("au au ")

class Gato(animal):
  def falar(self):
    print("miau!")

class Papagaio(animal):
  def move(self):
    print("aaaaaaaaaaaaaaaaaaaa!")

car1 = Cachorro("caramelo") 
boat1 = Gato("preto") 
plane1 = Papagaio("verde") 
pexe = peixe("crolido")

for x in (car1, boat1, plane1,pexe):
  print(x.cor)
 
  x.falar()
