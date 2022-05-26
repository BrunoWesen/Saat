# from akivymd.uix.datepicker import AKDatePicker
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
# from kivymd.app import MDApp
from picker import MDTimePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import get_color_from_hex as ku
from kivy.properties import ColorProperty
from kivy.uix.widget import Widget
from kivymd.uix.textfield import MDTextField
from PegData import AKDatePicker
from kivy.clock import Clock
from Tarefa import Tarefa
# from kivymd.uix.textfield import MDTextField
# from threading import Thread


class Box(Widget):
    cor = ColorProperty([1, 1, 1, 1])


class Subtarefa(FloatLayout):
    cont = 0

    def add_field(self):
        if self.cont == 0:
            sub = Campo_Texto(hint_text="Nome da subtarefa",
                              size_hint_x=.74,
                              pos_hint={"center_x": .5},
                              y=dp(220),
                              max_text_length=35)
            self.add_widget(sub)


        else:
            sub = Campo_Texto(hint_text="Nome da subtarefa",
                              size_hint_x=.74,
                              pos_hint={"center_x": .5},
                              y=dp(220),
                              max_text_length=35)

            self.add_widget(sub)
            for i in range(self.cont):
                i += 1
                self.children[i].y += dp(120)

        self.cont += 1

    def rem_field(self):
        if self.cont > 0:
            self.remove_widget(self.children[0])
            self.cont -= 1
            for i in range(self.cont):
                self.children[i].y -= dp(120)


class Campo_Texto(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.var = 0

    def on_focus(self, instance, focus, *args):
        super().on_focus()

        if focus == True:
            if len(self.text) == self.max_text_length and self.var == 0:
                self.event = Clock.schedule_interval(self.verificar_texto, 1 / 60)
                # t = Thread(target=self.verificar_texto, daemon=True)
                # self.event = Clock.schedule_once(self.verificar_texto)
                # t.daemon = True
                # t.start()
                self.var = 1

        if focus == False:
            if self.var == 0:
                pass
            else:
                self.event.cancel()
                self.var = 0
            # pass

    # def button_press():
    #     # create the thread to invoke other_func with arguments (2, 5)
    #     t = Thread(target=other_func, args=(2, 5))
    #     # set daemon to true so the thread dies when app is closed
    #     t.daemon = True
    #     # start the thread
    #     t.start()

    # def other_func(a, b):

    # your code here

    def verificar_texto(self, *args):
        # while len(self.text) >= self.max_text_length:
        #     self.text = self.text[:self.max_text_length]
        #     print("entrei")
        if len(self.text) > self.max_text_length:
            self.text = self.text[:self.max_text_length]
            # print("Problema")


class Formulario(MDScreen):
    tempo = 0
    tempo1 = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date = AKDatePicker(callback=self.callback)
        self.indice = 0
        self.data = 0
        self.indice2 = 0
        # self.date.year_range = [2021, 2036]

    def callback(self, date):
        if not date:
            return
        # date.text = "%d / %d / %d" % (date.day, date.month, date.year)
        # print(self.ids.date.text)
        self.data = f'{date.day}/{date.month}/{date.year}'
        self.ids.data.text = "Data: " + self.data
        # print(self.data)
        # pass

    def open(self):
        self.date.open()

    def postkv(self, app):
        # self.ids.boxl.remove_widget(self.ids.subtarefa)
        self.app = app

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "divider": None,
                "on_release": lambda x=f"{i}": self.set_item(x),
            } for i in range(1, 11)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=1.2,
            max_height=500,
        )
        self.menu.bind()

    def addWidget(self, app):

        if self.indice == 0:
            self.ids.boxl.add_widget(self.subtarefa)
            self.indice = 1
            if app.theme_cls.theme_style == 'Dark':
                self.ids.boxl.children[0].ids.boxcor1.cor = ku("#1f1f1f")

        else:
            self.indice = 0
            self.ids.boxl.remove_widget(self.ids.boxl.children[0])

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.ids.slider.value = self.ids.drop_item.current_item
        self.menu.dismiss()

    def on_pre_leave(self, *args):
        del self.subtarefa

    def on_enter(self, *args):
        self.subtarefa = Subtarefa()

    def on_pre_enter(self):

        if self.app.theme_cls.theme_style == 'Light':
            self.ids.boxcor.cor = ku("#f2f2f2")
            self.ids.nome.cor = ku("#dbdbdb")
            # self.ids.boxcor1.cor = ku("#f2f2f2")
            self.ids.nome1.cor = ku("#dbdbdb")
            try:
                self.ids.boxl.children[0].ids.boxcor1.cor = ku("#f2f2f2")
            except AttributeError:
                pass

        else:
            self.ids.boxcor.cor = ku("#1f1f1f")
            self.ids.nome.cor = ku("#404040")
            # self.ids.boxcor1.cor = ku("#1f1f1f")
            self.ids.nome1.cor = ku("#404040")
            try:
                self.ids.boxl.children[0].ids.boxcor1.cor = ku("#1f1f1f")
            except AttributeError:
                pass

    def adicionarbd(self):
        """
        # for i in self.ids.subtarefa.children:
        #     print(self.ids.subtarefa.children[0].text)
        if self.ids.nometarefa.text != "":
            nome = self.ids.nometarefa.text
        if self.ids.drop_item.text != "":
            importancia = self.ids.drop_item.text

        inicio = 1
        if self.ids.tempo1.text != "" and self.ids.tempo2.text != "":
            duracao = [self.ids.tempo1.text, self.ids.tempo2.text]
        """
        # print("Entrei")
        nome = ""
        inicio = 0
        fim = 0
        data = 0

        nometarefa = self.ids.nometarefa.text.split(" ")
        nometarefa = "".join(nometarefa)
        if nometarefa != "":
            nome = self.ids.nometarefa.text

        importancia = int(self.ids.slider.value)

        if self.tempo != 0:
            inicio = self.tempo
            # print(inicio)
            inicio = list(map(str, inicio))
            inicio = ":".join(inicio)

        if self.tempo1 != 0:
            fim = self.tempo1
            # print(fim)
            fim = list(map(str, fim))
            fim = ":".join(fim)

        duracao = self.ids.tempo1.text + " " + self.ids.tempo2.text
        duracao = duracao.split(" ")
        duracao = "".join(duracao)
        if duracao != "":
            hora = int(self.ids.tempo1.text)
            minuto = int(self.ids.tempo2.text)

            duracao = (hora * 60) + minuto

            if duracao > 1400:
                duracao = 1400

        if self.data != 0:
            data = self.data

        subtarefa = ""

        if nometarefa != "":
            tarefa = Tarefa()
            tarefa.inserir(nome, importancia, inicio, fim, duracao, data, subtarefa)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save)
        time_dialog.open()

    def on_save(self, instance, time):
        # print("Entrei no relogio")
        self.tempo = [time.hour, time.minute]
        timelabel = self.ids.labeltem

        timelabel.text = "Início:  " + f"{time.hour}:{time.minute}"

    def show_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save1)
        time_dialog.open()

    def on_save1(self, instance, time):
        self.tempo1 = [time.hour, time.minute]
        timelabel = self.ids.labeltem1

        timelabel.text = "Fim:  " + f"{time.hour}:{time.minute}"
