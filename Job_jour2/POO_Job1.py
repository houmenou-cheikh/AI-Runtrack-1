class Personne:
    """Classe définissant une personne caractérisée par :
        - son nom ;
        - son prénom ;
    """

    def __init__(self,nom = "Romancier",prenom= "Paul"):
        """Constructeur de notre classe"""

        self.nom = nom
        self.prenom = prenom
        

    def SePresenter(self):
        print('Mon nom est '+ self.nom)
        print("mon prenom est "+ self.prenom)
    
    #rajout accesseur
    def _get_name(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut nom"""

        print("on accede a l'attribut nom !")
        return self.nom

    def _get_last_name(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut nom"""

        print("on accede a l'attribut prenom !")
        return self.prenom

# rajout d'un mutateur
    def _new_name(self,newName):
        """ une methode qui modifie le nom"""
        print("le nouveau nom de {} est {}.".format(self.nom,newName))
        self.nom = newName

    def _new_Lastname(self,newLastName):
        """ une methode qui modifie le prenom"""
        print("le nouveau prenom de {} est {}.".format(self.nom,newLastName))
        self.nom = newLastName

#Instanciation des personne
personne1 = Personne("Cheikh", "Houmenou")
personne2 = Personne("Tampire","said")
personne3 = Personne("Pascal","Roxan")
personne4 = Personne()

#afficher avec print       
print(personne1.nom)
print(personne1.prenom)

#afficher par appel de methode
personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()

#affichage direct via le constructeur initial
personne4.SePresenter()

#afficher via l'accesseur
print(personne1._get_name())
print(personne1._get_last_name())
print(personne4._get_last_name())
print(personne4._get_name())

#affichage du mutateur pour le nom
personne1._new_name("Tidiane")
personne2._new_name("Terry")
personne3._new_name("Noemi")
personne4._new_name("Ramy")

#affichage du mutateur le prenom
personne1._new_Lastname("Ecole")
personne2._new_Lastname("Laplateforme")
personne3._new_Lastname("IA")
personne4._new_Lastname("School")

