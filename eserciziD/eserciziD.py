from typing import List


class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioD1 = Esercizio("EsercizioD1",1, "eserciziD/esercizioD1")
esercizioD2 = Esercizio("EsercizioD2",2, "eserciziD/esercizioD2")
esercizioD3 = Esercizio("EsercizioD3",3, "eserciziD/esercizioD3")

lista_eserciziD = [esercizioD1,esercizioD2,esercizioD3,]

def getEserciziD() -> List:
    return lista_eserciziD