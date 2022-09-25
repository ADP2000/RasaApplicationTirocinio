import os
import pymongo
from pymongo import MongoClient
import subprocess
import json
from typing import List
import requests
from random import randint
from eserciziA.eserciziA import lista_eserciziA
from eserciziC.eserciziC import lista_eserciziC
from eserciziD.eserciziD import lista_eserciziD
from eserciziE.eserciziE import lista_eserciziE
from eserciziH.eserciziH import lista_eserciziH

client = MongoClient("mongodb+srv://adp2000:provamongo@cluster0.3a73ecz.mongodb.net/?retryWrites=true&w=majority")
db = client.rasa
sessionResultCollection = db.sessionResult

class Esercizio: 
    def __init__(self, nome, livello,cartella) -> None:
        self.nome = nome
        self.livello = livello
        self.cartella = cartella

esercizioI = Esercizio("esercizioI", 1, "esercizioI")
lista_esercizi = lista_eserciziA + lista_eserciziC + lista_eserciziD + lista_eserciziE + lista_eserciziH
lista_esercizi.append(esercizioI)

levels = {
    1: [],
    2: [],
    3: []
}

for esercizio in lista_esercizi:
    levels[esercizio.livello].append(esercizio)

endpoint = "http://127.0.0.1:8000/session"        
risposta = requests.get(endpoint)
# with open("sessione.json", "w") as outfile:
#     json.dump(risposta,outfile,indent=4)

sessionID = risposta.json()['id']
esercizi = list(risposta.json()['exercises'])  #lista degli esercizi da somministrare con id, nome e livello

def getEsercizi(esercizi) -> List[Esercizio]:
    nomiEsercizi = []
    for e in esercizi:
        nomiEsercizi.append(e['name'])

    eserciziDaSvolgere = []
    for ne in nomiEsercizi:
        for esercizio in lista_esercizi:
            if ne == esercizio.nome:
                eserciziDaSvolgere.append(esercizio)
    
    return eserciziDaSvolgere

eserciziScelti = getEsercizi(esercizi)
# f = open("feedback_{}.txt".format(sessionID), "w")
# f.write("SESSION ID = {}".format(sessionID))
# f.close()

feedbackData = {
    "cognitiveExerciseResult": []
}

with open("feedback.json", "w") as outfile:         # file json in cui viene salvato il feedback.
                                                    # All'inizio è pari alla lista vuota
    json.dump(feedbackData,outfile,indent=4)

i = -1
for esercizio in eserciziScelti:
    i += 1
    with open("esercizio.json","w") as outfile:      # file json in cui viene salvato l'esercizio corrente
        json.dump(esercizi[i],outfile,indent=4)

    f = open("cartellaEsercizio.txt", "w")
    f.write(esercizio.cartella)
    f.close()

    cartellaCorrente = os.getcwd()
    os.chdir(esercizio.cartella)
    comando = "docker build . -t adp2000/prova_rasa:{}"
    subprocess.run(comando.format(esercizio.nome), shell=True)  # permette di costruire l'immagine dell'
                                                                        # esercizio scelto ed eseguire il comando successivo
    subprocess.run("docker-compose up -d", shell=True) # il comando docker-compose up esegue i container che si 
                                                        # riferiscono ai server e il parametro -d li esegue in background 
    os.chdir(cartellaCorrente)
    subprocess.run("py rasaShell.py", shell=True)  # esegue il file rasaShell.py che permette di eseguire l'esercizio
                                                        # e si occupa della sucessiva deattivazione dei server
    #subprocess.run("py rasaHTTP.py", shell=True)    # esegue il file rasaHTTP.py

data = json.load(open("feedback.json"))
sessionResult = data
sessionResult['_id'] = sessionID
result = sessionResultCollection.insert_one(sessionResult)
# requests.post(endpoint,json=data)