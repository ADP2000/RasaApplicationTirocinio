import os
import subprocess
from random import randint
from eserciziA.eserciziA import lista_eserciziA
from eserciziC.eserciziC import lista_eserciziC
from eserciziD.eserciziD import lista_eserciziD
from eserciziE.eserciziE import lista_eserciziE
from eserciziH.eserciziH import lista_eserciziH

class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella

esercizioI = Esercizio("EsercizioI", 1, "esercizioI")
lista_esercizi = lista_eserciziA + lista_eserciziC + lista_eserciziD + lista_eserciziE + lista_eserciziH
lista_esercizi.append(esercizioI)

levels = {
    1: [],
    2: [],
    3: []
}

for esercizio in lista_esercizi:
    levels[esercizio.livello].append(esercizio)

def scegli_esercizio(livello) -> Esercizio:
    lista = levels[livello]
    i = randint(0,len(lista)-1)
    return lista[i]

n = input("Scegli il livello di difficota da 1 a 3:")
numero = int(n)
esercizioScelto = scegli_esercizio(numero)
print(esercizioScelto.nome)
f = open("cartellaEsercizio.txt", "w")
f.write(esercizioScelto.cartella)
f.close()
f = open("nomeEsercizio.txt", "w")
f.write(esercizioScelto.nome)
f.close()
# print(os.getcwd())   # restituisce la directory corrente
# print(os.listdir())  # restituisce le cartelle e i file contenuti nella directory corrente   
# os.chdir("C:/Users/Antonio/Tirocinio/RasaApplication/" + esercizioScelto.cartella) # cambia la directory corrente
# print(os.getcwd())
comando1 = "docker start {}_app_1"
comando2 = "docker start {}_rasa_1"
subprocess.run(comando1.format(esercizioScelto.nome.lower()), shell=True)  #esegue il comando dal terminale
subprocess.run(comando2.format(esercizioScelto.nome.lower()), shell=True)  #esegue il comando dal terminale
subprocess.run("py rasaShell.py", shell=True)  #esegue il file rasaShell.py che permette di eseguire l'esercizio
                                               # e si occupa della sucessiva deattivazione dei server
