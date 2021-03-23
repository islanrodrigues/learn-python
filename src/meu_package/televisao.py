class Televisao:
  def __init__(self):
    self.esta_ligada = False
    self.canal = 1
  
  def power(self): 
    if self.esta_ligada:
      self.esta_ligada = False
    else:
      self.esta_ligada = True
    
    def aumentarCanal(self):
      if self.canal < 30 and self.esta_ligada:
        self.canal += 1
    
    def diminuirCanal(self):
      if self.canal > 1 and self.esta_ligada:
        self.canal -= 1