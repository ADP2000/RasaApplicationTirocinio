from typing import List


class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella


esercizioE11 = Esercizio("esercizioE11",1, "eserciziE/esercizioE11")
esercizioE12 = Esercizio("esercizioE12",1, "eserciziE/esercizioE12")
esercizioE13 = Esercizio("esercizioE13",1, "eserciziE/esercizioE13")
esercizioE21 = Esercizio("esercizioE21",2, "eserciziE/esercizioE21")
esercizioE22 = Esercizio("esercizioE22",2, "eserciziE/esercizioE22")
esercizioE23 = Esercizio("esercizioE23",2, "eserciziE/esercizioE23")
esercizioE31 = Esercizio("esercizioE31",3, "eserciziE/esercizioE31")
esercizioE32 = Esercizio("esercizioE32",3, "eserciziE/esercizioE32")
esercizioE33 = Esercizio("esercizioE33",3, "eserciziE/esercizioE33")
lista_eserciziE = [esercizioE11, esercizioE12,esercizioE13,
esercizioE21,esercizioE22, esercizioE23, esercizioE31, esercizioE32, esercizioE33]

def getEserciziE() -> List:
    return lista_eserciziE