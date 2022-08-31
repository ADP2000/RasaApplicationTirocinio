import os
import subprocess

f = open("cartellaEsercizio.txt","r")
cartella = f.read()
f.close()
# f = open("nomeEsercizio.txt", "r")
# nome = f.read()
# f.close()

os.chdir(cartella) # cambia la directory corrente
print(os.getcwd())
subprocess.run("rasa shell", shell=True)
# subprocess.run(comando1.format(nome.lower()), shell=True)
# subprocess.run(comando2.format(nome.lower()), shell=True)
subprocess.run("docker-compose stop", shell=True)