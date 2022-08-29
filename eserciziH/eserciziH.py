from typing import List


class Esercizio: 
    def __init__(self, nome, livello, cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioH1 = Esercizio("EsercizioH1",3, "eserciziH/esercizioH1")
esercizioH2 = Esercizio("EsercizioH2",2, "eserciziH/esercizioH2")
esercizioH3 = Esercizio("EsercizioH3",2, "eserciziH/esercizioH3")
esercizioH4 = Esercizio("EsercizioH4",2, "eserciziH/esercizioH4")

lista_eserciziH = [esercizioH1,esercizioH2,esercizioH3,esercizioH4]

def getEserciziH() -> List:
    return lista_eserciziH