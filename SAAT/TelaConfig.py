from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class TelaConfig(MDScreen):
    i = 0

    def alterar_texto_tema(self):

        if self.ids.tema.text == "Tema atual: Claro":
            self.ids.tema.text = "Tema atual: Escuro"

        else:
            self.ids.tema.text = "Tema atual: Claro"

    def postkv(self, app):
        self.app = app

    def on_pre_enter(self, *args):

        if self.i == 0:

            if self.app.theme_cls.theme_style == "Light":
                self.ids.tema.text = "Tema atual: Claro"

            else:
                self.ids.tema.text = "Tema atual: Escuro"

            self.i = 1
