from typing import List


class Esercizio: 
    def __init__(self, nome, livello, cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioH1 = Esercizio("esercizioH1",3, "eserciziH/esercizioH1")
esercizioH2 = Esercizio("esercizioH2",2, "eserciziH/esercizioH2")
esercizioH3 = Esercizio("esercizioH3",2, "eserciziH/esercizioH3")
esercizioH4 = Esercizio("esercizioH4",2, "eserciziH/esercizioH4")

lista_eserciziH = [esercizioH1,esercizioH2,esercizioH3,esercizioH4]

def getEserciziH() -> List:
    return lista_eserciziH