from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
Window.size = (400, 620)


KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        MDLabel:
            text: "Bonjour"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Cliquez-moi"
            pos_hint: {'center_x': 0.5}
            on_release: app.show_dialog()
'''


class MainScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_dialog(self):
        dialog = MDDialog(
            text="Ceci est un MDDialog",
            buttons=[
                MDRaisedButton(
                    text="FERMER",
                    on_release=lambda x: self.close_dialog(dialog)
                )
            ]
        )
        dialog.open()

    def close_dialog(self, dialog):
        dialog.dismiss()


if __name__ == '__main__':
    MyApp().run()
