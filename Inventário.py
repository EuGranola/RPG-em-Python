from MãeItem import Item
from FilhaPoção import Pocao
from FilhaArma import Arma

mochila = [
    Pocao("Poção polisuco", 1, 50, 20),
    Arma("Katana Vingadora", 5, 100, 15),
    Item("Pedra filosofal", 2, 10)
]
for item in mochila:
    item.usar()