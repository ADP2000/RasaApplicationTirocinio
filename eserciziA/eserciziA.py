from typing import Dict, List
class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella
        


esercizioA1 = Esercizio("EsercizioA1", 1, "eserciziA/esercizioA1")
esercizioA2 = Esercizio("EsercizioA2",2, "eserciziA/esercizioA2")
esercizioA3 = Esercizio("EsercizioA3",3, "eserciziA/esercizioA3")
esercizioA4 = Esercizio("EsercizioA4",2, "eserciziA/esercizioA4")

lista_eserciziA = [esercizioA1,esercizioA2,esercizioA3,esercizioA4]

def getEserciziA() -> List:
    return lista_eserciziA