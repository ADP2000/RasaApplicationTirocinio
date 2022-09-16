import os
import subprocess
import json


data = json.load(open("sessione.json"))

f = open("cartellaEsercizio.txt","r")
cartella = f.read()
f.close()
cartellaCorrente = os.getcwd()

os.chdir(cartella) # cambia la directory corrente
subprocess.run("rasa shell", shell=True)
f = open("errori.txt", "r")
errori = f.read()
f.close()

subprocess.run("docker-compose stop", shell=True)

os.chdir(cartellaCorrente)
f = open("nomeEsercizio.txt", "r")
esercizio = f.read()
f.close()

f = open("feedback_{}.txt".format(data['id']),"a")
f.write("\nE' stato svolto l'{} con numero di errori pari a {}".format(esercizio,errori))
f.close()