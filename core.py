import ampalibe
from ampalibe import Messenger, Payload, translate, Model
from ampalibe.ui import QuickReply, Button, Type, Element
from conf import Configuration as config
from ampalibe.messenger import Filetype
from requete import Requete

chat = Messenger()
query = Model()
req  = Requete(config())

# create a get started option to get permission of user.
# chat.get_started()
print(config.APP_URL)

@ampalibe.command('/')
def main(sender_id, cmd, **ext):
    chat.get_started()
    chat.send_text(sender_id, "Bienvenue chez MenuViz👌😊🍕 !")
    chat.send_text(sender_id, "Explorez notre gamme de fonctionnalités, laissez libre cours à votre créativité et transformez vos menus en une véritable expérience visuelle. Nous sommes là pour vous guider à chaque étape et vous aider à créer des menus qui raviront vos clients et renforceront votre image de marque.")
    persistent_menu = [
        Button(
            type = Type.postback,
            title = "Voir tous les menus📑",
            payload = Payload("/menus")
        ),
        Button(
            type = Type.postback,
            title = "Rechercher un menu",
            payload = Payload("/menu")
        )

    ]
    chat.persistent_menu(sender_id, persistent_menu)
    query.set_action(sender_id, None)

@ampalibe.command('/menus')
def GetAllMenus(sender_id, cmd, **ext):
    chat.send_text(sender_id, "Voici tous les menus de notre carte!")
    """
    Afficher la liste des menus à partir de la requete
    """
    menus = req.Get_Menus()
    data = []
    i = 0
    while i < len(menus):
        image = menus[i][2]
        print(data)
        button = [
            Button(
                type = Type.postback,
                title = "Visualiser le menu",
                payload = Payload("/qrcode", id_vacc= str(menus[i][0]))
            )
        ]
        data.append(
            Element(
                title = str(i+1) + "-" + menus[i][1],
                subtitle = menus[i][3],
                image_url = config.APP_URL + f"/asset/{image}",
                buttons = button,
            )
        )
        i = i+1
        
    chat.send_template(sender_id, data, next=True )
    

