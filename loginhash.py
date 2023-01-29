import hashlib
import os

os.system("clear")


print("Bienvenido al sistema de verificacion")

ctr=str(input("Coloque su contraseña: "))
hashes=hashlib.sha256(bytes(ctr, encoding='utf-8')).hexdigest()
if hashes=="hashdelacontraseña":
    print("Bienvenido usuario")
else:
    print("Contraseña incorrecta, intentelo en otra oportunidad.")
    exit()