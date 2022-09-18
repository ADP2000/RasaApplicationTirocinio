from typing import Dict, List

class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioC1 = Esercizio("esercizioC1",1, "eserciziC/esercizioC1")
esercizioC2 = Esercizio("esercizioC2",2, "eserciziC/esercizioC2")
esercizioC3 = Esercizio("esercizioC3",3, "eserciziC/esercizioC3")

lista_eserciziC = [esercizioC1,esercizioC2,esercizioC3,]

def getEserciziC() -> List:
    return lista_eserciziC
