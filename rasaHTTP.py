import os
import subprocess

f = open("cartellaEsercizio.txt","r")
cartella = f.read()
f.close()

os.chdir(cartella) # cambia la directory corrente
subprocess.run("python -m http.server", shell=True)
#subprocess.run("docker-compose stop", shell=True)