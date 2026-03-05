class Employe:
    def __init__(self,nm_permis,nom,prenom):
        self.nm_permis=nm_permis
        self.nom=nom
        self.prenom=prenom
        self.voiture_service=None
    def afficher(self):
        print(f"le nom de la personne est:{self.nom}{self.prenom},son numero de permis est:{self.nm_permis}")
        if self.voiture_service:
            print("voiture attribuee")
        else:
            print("auucne voiture attribuee")
    def affectuer(self,voiture):
        if self.voiture_service:
            print("cet employe possede deja une voiture")
            return
        if self.voiture.chauffeur is not None:
            print("cette voiture est deja attribuee")
            return
        self.voiture_service=voiture
        voiture.chauffeur=self
class Voiture:
    def __init__(self,matricule,annee,marque,km):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.km=km
        self.chauffeur=None
    def afficher(self):
        print(f"la matricule est{self.matricule},annee est:{self.annee},marque est:{self.marque},le kilometrage est:{self.km}")
        if self.chauffeur:
            print(f"le chauffeur est:{self.chauffeur}")
        else:
            print("aucune chauffeur")
    