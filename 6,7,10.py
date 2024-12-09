class Cachorro:

  def falar(self):
    print("au au!")

class gato:
  

  def falar(self):
    print("miau!")
    
class papagaio:
    def falar(self):
        print("ola!")
        
pap = papagaio()
cac = Cachorro()       
cat = gato() 


for x in (cac, cat, pap):
  x.falar()
