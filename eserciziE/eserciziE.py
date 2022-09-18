from typing import List


class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioE1 = Esercizio("esercizioE1",1, "eserciziE/esercizioE1")
esercizioE2 = Esercizio("esercizioE2",2, "eserciziE/esercizioE2")
esercizioE3 = Esercizio("esercizioE3",3, "eserciziE/esercizioE3")

lista_eserciziE = [esercizioE1,esercizioE2,esercizioE3,]

def getEserciziE() -> List:
    return lista_eserciziE