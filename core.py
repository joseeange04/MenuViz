import ampalibe
from ampalibe import Messenger, Payload, translate, Model
from ampalibe.ui import QuickReply, Button, Type, Element
from conf import Configuration as config
from ampalibe.messenger import Filetype

chat = Messenger()
query = Model()

# create a get started option to get permission of user.
# chat.get_started()

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

