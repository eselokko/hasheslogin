import hashlib
import os

os.system("clear")


print("Bienvenido al sistema de verificacion")

ctr=str(input("Coloque su contraseña: "))
hashes=hashlib.sha256(bytes(ctr, encoding='utf-8')).hexdigest() # la libreria soporta todo tipo de encriptación SHA, blake y MD5. si busca cambiarlo, reemplace 'sha256' por la encriptación disponible que desea.
if hashes=="0573df7b697c8325c2716d00a57962c9c2077595940bf38248dfdd86efb2e001": # aca va tu hash (hash puesto: acavatuhash)
    print("Bienvenido usuario")
else:
    print("Contraseña incorrecta, intentelo en otra oportunidad.")
    exit()
