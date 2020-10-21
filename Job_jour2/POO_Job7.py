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
        print('nom: '+ self.nom)
        print("prenom: "+ self.prenom)


class Client(Personne):

    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom =prenom
        self.collection = ()
    
    def inventaire(self):
        for book in self.collection.items():
            print(book)

class Bibliotheque:
    """une classe bibliotheque"""

    def __init__(self,nom, catalogue):
        self.nom = nom
        self.catalogue = {}
        self.oeuvre = []

    def acheterLivre(self,auteur,titre,nbr):
        self.titre = titre 
        self.nbr = nbr

        if self.titre in self.oeuvre:
            try:
                self.catalogue[self.titre] += nbr
            except:
                self.catalogue[self.titre] = nbr
        else:
             print("Pas de livre pour ce titre")

    def inventaire(self):
        print("consultation du catalogue:\n")
        for elt in self.catalogue.items():
            print(elt)

    def louer(self,Client,titre):
        self.panierClient = []
        if self.titre in self.catalogue:
            self.panierClient.append(self.titre)
            self.catalogue[self.titre] -= 1
        else:
            print("ce livre n'est pas encore disponible dans la Bibliotheque")

    def rendreLivre(self,Client):
        self.collection = []
        if len(self.collection) != 0:
            for titre in self.collection:
                if titre in self.catalogue:
                    self.catalogue[titre] += 1
        else:    
            print("vous n'avez pas de livre à rendre") 
    

x1=Bibliotheque("Axel",{"Life good":5})

x1.acheterLivre("Axel","Life good",2)
x1.acheterLivre("Axel","Life good",2)

x1.inventaire()
x1.louer("Aba","Life good")
x1.rendreLivre("Abo")

