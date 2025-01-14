#from poo import Voiture as Voit
#import poo
from exceptions import VideException
from poo import Voiture, CONSO_MAX

CONSO_MAX = 12
print(CONSO_MAX)

#Exception
try:
    v = Voiture("Audi", "Q3", 5)
    v.modele = ""
    print(v)
except VideException as e:
    print(f"Exception: {e}")
except Exception:
    print("Grosse erreur")
finally:
    print("Toujours exécuté")