import os
import subprocess
import json

f = open("cartellaEsercizio.txt","r")
cartella = f.read()
f.close()
cartellaIniziale = os.getcwd()

os.chdir(cartella) # cambia la directory corrente
subprocess.run("rasa shell", shell=True)
f = open("errori.txt", "r")
errori = int(f.read())
f.close()

subprocess.run("docker-compose stop", shell=True)

os.chdir(cartellaIniziale)

esercizio = json.load(open("esercizio.json"))
data = json.load(open("feedback.json"))
# sessionId = data['id']
listaEsercizi = list(data['cognitiveExerciseResult'])
listaEsercizi.append({
    "id": esercizio['id'],
    "score": errori
})

with open("feedback.json", "w") as outfile:             # viene salvato nel file feedback.json la lista
                                                        # aggiornata degli esercizi svolti con id e score
    # json.dump({ "id": sessionId, "exercises": listaEsercizi }, outfile, indent=4)
    json.dump({"cognitiveExerciseResult": listaEsercizi }, outfile, indent=4)