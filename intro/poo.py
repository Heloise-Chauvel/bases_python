from abc import ABC, abstractmethod
from exceptions import VideException

#variable de module
CONSO_MAX = 10

class Vehicule(ABC):
    def __init__(self, marque, modele):
        self.marque = marque #public
        self.modele = modele #privé

    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self, valeur):
        '''
        définir le modèle

        Raises:
            VideException: si le modèle est vide
        :param valeur:
        :return:
        '''
        if valeur != "":
            self.__modele = valeur
        else:
            raise VideException("modele")

    @abstractmethod
    def demarrer(self):
        pass

    def __str__(self):
        return f"La voiture {self.marque} {self.modele}"

class Voiture(Vehicule):
    def __init__(self, marque, modele, nb_portes):
        super().__init__(marque, modele)
        self.nb_portes = nb_portes

    def __str__(self):
        return f"{super().__str__()} et {self.nb_portes}"

    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} démarre.")


