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

n = input("Scegli il livello di difficota da 1 a 3: ")
numero = int(n)
if(numero > 3):
    print("Hai sbagliato numero. Deve essere compreso tra 1 e 3!")
else:
    esercizioScelto = scegli_esercizio(numero)
    print(esercizioScelto.nome)

    f = open("cartellaEsercizio.txt", "w")
    f.write(esercizioScelto.cartella)
    f.close()

    # f = open("nomeEsercizio.txt", "w")
    # f.write(esercizioScelto.nome)
    # f.close()

    cartellaCorrente = os.getcwd()
    os.chdir(esercizioScelto.cartella)
    comando = "docker build . -t adp2000/prova_rasa:{}"
    subprocess.run(comando.format(esercizioScelto.nome), shell=True)  # permette di costruire l'immagine dell'
                                                                    # esercizio scelto ed eseguire il comando successivo
    subprocess.run("docker-compose up -d", shell=True) # il comando docker-compose up esegue i container che si 
                                                    # riferiscono ai server e il parametro -d li esegue in background 
    os.chdir(cartellaCorrente)
    subprocess.run("py rasaShell.py", shell=True)  # esegue il file rasaShell.py che permette di eseguire l'esercizio
                                                    # e si occupa della sucessiva deattivazione dei server
    #subprocess.run("py rasaHTTP.py", shell=True)    # esegue il file rasaHTTP.py