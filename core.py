import ampalibe
from ampalibe import Messenger, Payload, translate, Model
from ampalibe.ui import QuickReply, Button, Type, Element
from conf import Configuration as config
from ampalibe.messenger import Filetype
from requete import Requete
import qrcode
import os

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
                payload = Payload("/qrcode", id_menu= str(menus[i][0]), nom_menu = str(menus[i][1]))
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
    
@ampalibe.command('/qrcode')
def Get_QRCode(sender_id, id_menu, nom_menu, **ext):
    personas = chat.get_personas(876103446353988)
    data = personas['name'], id_menu, nom_menu
    print(data)

    qr = qrcode.make(data)
    qr.show()
    menu_file = nom_menu.replace(" ", "")
    file_name = f"{menu_file}qr.png"
    image_path = f"assets/public/{file_name}"
    

    if os.path.exists(image_path):
        print("L'image QR existe déjà.")
    else:
        print("L'image QR n'existe pas.")
        qr.save(image_path)

    chat.send_text(sender_id, "Découvrez une expérience immersive en scannant ce QR code avec l'application FoodScope ! Vous pourrez ainsi visualiser en temps réel le plat que vous êtes sur le point de commander. Plongez-vous dans une expérience visuelle captivante et laissez-vous transporter par la magie de la réalité augmentée pour une expérience culinaire unique.")
    chat.send_file(sender_id, image_path, reusable=True)