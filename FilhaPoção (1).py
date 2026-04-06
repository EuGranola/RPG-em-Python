from MãeItem import Item

class Pocao (Item):
    def __init__ (self, nome, peso, preco, PontosDeHP):
        super ().__init__ (nome, peso, preco)
        self.PontosDeHP= PontosDeHP
    def usar (self):
        print (f"Você bebe {self.nome} e recupera {self.PontosDeHP} de HP.")