import os
import subprocess

f = open("cartellaEsercizio.txt","r")
cartella = f.read()
f.close()
f = open("nomeEsercizio.txt", "r")
nome = f.read()
f.close()
comando1 = "docker stop {}_app_1"
comando2 = "docker stop {}_rasa_1"
os.chdir("C:/Users/Antonio/OneDrive/Documenti/GitHub/RasaApplicationTirocinio" + cartella) # cambia la directory corrente
print(os.getcwd())
subprocess.run("rasa shell", shell=True)
subprocess.run(comando1.format(nome.lower()), shell=True)
subprocess.run(comando2.format(nome.lower()), shell=True)