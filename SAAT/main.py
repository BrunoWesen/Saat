# coding: "utf-8"
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManagerException
from kivymd.app import MDApp
# from kivymd.uix.picker import MDTimePicker
from kivymd.uix.dialog import MDDialog
from kivy.storage.jsonstore import JsonStore
from akivymd.uix.statusbarcolor import change_statusbar_color
# from threading import Thread
from Formulario import Formulario

class Programa(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore("Config.json")
        self.x = self.store["font"]["name"]
        if self.x == "Padrão":
            self.fonte = "Roboto"
        else:
            self.fonte = self.x
            Clock.schedule_once(self.carregar_fonte)

        self.indice = self.store["cortema"]["i"]
        self.indice2 = self.store["font"]["i2"]
        # del self.x Assim que deleta uma variável/objeto que não está em uso
        self.theme_cls.theme_style = self.store["tema"]["tema"]
        self.theme_cls.primary_palette = self.store["cortema"]["tema"]
        change_statusbar_color(self.theme_cls.primary_color)

        # Threads
        # self.instances = Thread(target=self.instanciar, daemon=True)
        # t = Thread(target=self.iniciar, daemon=True)
        # t2 = Thread(target=self.carregar_fonte, daemon=True)
        # t3 = Thread(target=self.desenhar_telas, daemon=True)

        # Startando as Threads
        # t.start()
        # t2.start()
        # t3.start()

        # Clock.schedule_once(self.iniciar)
        # Clock.schedule_once(self.ThreadCall, 15)
        # print("começou aqui")

    # def desenhar_telas(self):
    #     pass
    # print("entrei")
    def addForm(self, *args):
        self.form = Formulario(name="Adicionar Tarefa")

    def transAT(self, manager):
        try:
            manager.add_widget(self.form)
            manager.current = "Adicionar Tarefa"
        except ScreenManagerException:
            manager.current = "Adicionar Tarefa"

    def transCFG(self, manager):
        try:
            manager.add_widget(self.tcfg)
            manager.current = "telaconfig"
        except ScreenManagerException:
            manager.current = "telaconfig"

    #     pass

    def alterar_fonte(self):
        def my_callback(store, key, result):
            pass

        fontes = ["Padrão", "Calibri", "Comic", "Georgia", "Verdana"]

        if self.indice2 < 4:
            self.indice2 += 1

        else:
            self.indice2 = 0

        dialog = MDDialog(text="Para aplicar a nova fonte: %s, será preciso reiniciar a aplicação!" %
                               fontes[self.indice2])
        dialog.open()

        self.store.async_put(callback=my_callback, key='font', name='%s' % fontes[self.indice2], i2=self.indice2)

    def alterar_modo(self):
        def my_callback(store, key, result):
            pass

        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

        self.store.async_put(my_callback, "tema", tema=self.theme_cls.theme_style)

    def alterar_tema(self):
        def my_callback(store, key, result):
            pass

        if self.indice < 18:
            self.indice += 1
        else:
            self.indice = 0
        i = self.indice
        self.theme_cls.primary_palette = self.temas[i]
        change_statusbar_color(self.theme_cls.primary_color)
        self.store.async_put(my_callback, "cortema", tema=self.theme_cls.primary_palette, i=self.indice)

    """
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save)
        time_dialog.open()

    def on_save(self, instance, time):
        # time = time
        # instancia = instance
        # tempo = [time.hour, time.minute, instancia.am_pm]
        # print(tempo)
        pass

    def show_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save1)
        time_dialog.open()

    def on_save1(self, instance, time):
        # time = time
        # instancia = instance
        # tempo1 = [time.hour, time.minute, instancia.am_pm]
        # print(tempo1)
        pass

    # def show_date_picker(self):
    #     date_dialog = MDDatePicker()
    #     date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
    #     date_dialog.open()
    """

    def show_alert_dialog(self):
        dialog = MDDialog(text="SAAT versão 0.4.10\nFeito por: Bruno Sevalho e\nGabriely da Mata")
        dialog.open()

    def carregar_fonte(self, *args):
        from kivy.core.text import LabelBase

        if self.fonte == "Calibri":
            LabelBase.register(name="Calibri", fn_regular="fontes/calibri.ttf", fn_bold="fontes/calibrib.ttf")

        elif self.fonte == "Comic":
            LabelBase.register(name="Comic", fn_regular="fontes/comic.ttf", fn_bold="fontes/comicbd.ttf")

        elif self.fonte == "Georgia":
            LabelBase.register(name="Georgia", fn_regular="fontes/georgia.ttf", fn_bold="fontes/georgiab.ttf")

        else:
            LabelBase.register(name="Verdana", fn_regular="fontes/verdana.ttf", fn_bold="fontes/verdanab.ttf")

    # def instanciar(self):
    #     def add():
    #         MDApp.get_running_app().root.ids.Gerenciador \
    #             .add_widget(form)
    #
    #         MDApp.get_running_app().root.ids.Gerenciador \
    #             .add_widget(tcfg)

        # Clock.schedule_once(add, 10)
        # raise IndexError

    def on_start(self):
        from TelaConfig import TelaConfig
        self.tcfg = TelaConfig(name="telaconfig")
        self.form = Formulario(name="Adicionar Tarefa")

        self.temas = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal',
                      'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray',
                      'BlueGray']

        # self.instances.start()

        # MDApp.get_running_app().root.ids.Gerenciador \
        #     .add_widget(TelaConfig(name="telaconfig"))

    #     print("Depois veio aqui")
    #     self.fps_monitor_start()

    # def build(self):
    #     print("Mentira, começou aqui")
    #     return Builder.load_file("Programa.kv")


if __name__ == "__main__":
    Programa().run()
