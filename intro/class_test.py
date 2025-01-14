import json

class Personne:
    '''
    def __init__(self, nom, age, description:str=None):
        self.__nom = nom
        self.__age = age
        if description is not None:
            self.description = description
    '''

    def __init__(self, **kwargs):
        self.__nom = kwargs['nom']
        self.__age = kwargs['age']
        if 'description' in kwargs.keys():
            self.description = kwargs['description']

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    #représentation chaine de caractères de l'objet simple
    def __str__(self):
        return self.__nom

    # réprésetation détaillée de l'objet
    def __repr__(self):
        return json.dumps(self.__dict__, indent=3)

pers = Personne(nom="Héloïse", age="30")
print(pers.get_nom())
print(pers.age)
pers.age = 31
print(pers.age)
print(pers)
print(repr(pers))