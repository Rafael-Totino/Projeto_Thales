from tkinter import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pathlib
import os
import shutil
import time
import json
from main_functions import *


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

    def save_infos(self):
        exec_period = 1
        regx = self.ids.input_regx.text
        origin_folder = self.ids.input_folder_origin.text
        dest_folder = self.ids.input_folder_dest.text

        if (exec_period == " " or regx == " " or origin_folder == " " or dest_folder == " "):
            # Pop-up de alerta de campos vazios, "salvamento mal sucedido, tente novamente com todos os campos preenchidos"
            ...

        else:
            write_config_file(exec_period, regx, origin_folder, dest_folder)

    def switch_click(self, switchObject, switchValue):
        if (switchValue):
            self.ids.my_label.text = "The aplication is runnig ...  until switch is turn OFF "
        else:
            self.ids.my_label.text = "You stoped the aplication, if you want to continue, turn the switch ON"


class MainApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MainApp().run()
