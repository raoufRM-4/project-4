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
        