from ampalibe import Model
class Requete (Model):
    def __init__(self, conf):
        """
            Connexion à notre base de donnée
        """
        Model.__init__(self, conf)

    @Model.verif_db
    def Get_Menus(self):
        """
        Recupérer les menus de la carte
        """
        req = """
                SELECT id_menu, nom_plat, image, prix
                FROM menus_carte
        """
        self.cursor.execute(req)
        result = self.cursor.fetchall()
        self.db.commit()
        return result