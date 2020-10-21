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
    

class Auteur(Personne):
    """ une classe auteur"""

    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.oeuvre = []

    def listerOeuvre(self):

        if len(self.oeuvre) != 0:
            print("liste des livres de "+ self.nom)
            for book in self.oeuvre:
                 book.Print_()
        else:
            print("l auteur a 0 livre")
       
    def ecrireUnLivre(self,titre):
        self.titre = titre
        newBook = Livre(titre,self)
        self.oeuvre.append(newBook)
        
class Livre():
    """une classe livre"""

    def __init__(self,titre,auteur):
        self.titre = titre
        self.auteur = Auteur("Anais","Marrant") 

    def Print_(self):
        print(' _titre du livre est '+ self.titre)
        


livre1 = Livre("Vol de nuit","Anais")
livre1.Print_()

auteur1 = Auteur("Alpha", "Beta")
auteur1.ecrireUnLivre("Soleil du savent")
auteur1.ecrireUnLivre("Science et etude")
auteur1.listerOeuvre()

auteur2 = Auteur("Alpha2", "Beta2")
auteur2.ecrireUnLivre("Le petit Francais")
auteur2.listerOeuvre()

auteur3 = Auteur("Ferdinand", "Oyono")
auteur3.ecrireUnLivre("Geolocalisation")
auteur3.ecrireUnLivre("LaPlateforme_")
auteur3.ecrireUnLivre("Intelligence Artificielle")
auteur3.ecrireUnLivre("Une vie de boy")
auteur3.listerOeuvre()

