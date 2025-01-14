'''
Documentation
Nom de classe en camelCase
Tout le reste en snakeCase

'''
nom: str = "Héloïse"
nom2: str = 'Marie'
age: float = 31
isPres: bool = False #camelCase

def presentation():
    if isPres:
        print(f"Bonjour je suis {nom}, j'ai {age} ans")    
    elif age > 30:
        print("Je suis Héloïse du futur")
    else:
        print("Il n'y a personne")

presentation()