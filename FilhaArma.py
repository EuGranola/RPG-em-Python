from MãeItem import Item

class Arma(Item):
    def __init__(self, nome, peso, preco, dano_de_ataque):
        super().__init__(nome, peso, preco)
        self.dano_de_ataque = dano_de_ataque
    def usar(self):
        print(f"Você ataca com {self.nome} e causa {self.dano_de_ataque} de dano.")