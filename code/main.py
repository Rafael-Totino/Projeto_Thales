
from main_functions import *
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from tkinter import messagebox

# --------------------------------------------------
# Main UI widget class
# --------------------------------------------------


class MyBoxLayout(BoxLayout, GridLayout, FloatLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

    # --------------------------------------------------
    # function called when clicking save button
    # checks if the fields are blank and raises an alert
    # if not, call the function that writes the config file
    # --------------------------------------------------
    def save_infos(self):
        exec_period = 1
        regx = str(self.ids.input_regx.text)
        origin_folder = str(self.ids.input_folder_origin.text)
        dest_folder = str(self.ids.input_folder_dest.text)

        if (exec_period == "" or regx == "" or origin_folder == "" or dest_folder == ""):
            # Pop-up de alerta de campos vazios, "salvamento mal sucedido, tente novamente com todos os campos preenchidos"
            messagebox.showinfo('Alerta campos vazios',
                                'Os campos de informações estão vazios \n O salvamento de novas informações foi mal sucedido, \n tente novamente com todos os campos preenchidos')

        else:
            write_config_file(exec_period, regx, origin_folder, dest_folder)

    # --------------------------------------------------
    # call function when turning the switch on and off
    # read the config.json informations
    # If ON, execute the rotines with a timer loop
    # If OFF, wait for the user
    # --------------------------------------------------
    def switch_click(self, switchObject, switchValue):
        with open('config.json', 'r', encoding='utf8') as f:
            dados = json.load(f)

        prefix_archive = dados['regx']
        path_A = dados['folder_origin']
        path_B = dados['folder_dest']
        execution_time = dados['execution_period']

        if (switchValue == True and (self.ids.input_regx.text != "" or self.ids.input_folder_origin.text != "" or self.ids.input_folder_dest.text != "" or execution_time != "")):
            self.ids.my_label.text = "The aplication is runnig ...  until switch is turn OFF "
            main(execution_time, path_A, prefix_archive, path_B)
            MyBoxLayout.switch_click(self, switchObject, switchValue)
        else:
            self.ids.my_label.text = "You stoped the aplication, verify if the input boxes are not empty and try again"
            time.sleep(1)
            MyBoxLayout.switch_click(self, switchObject, switchValue)

# --------------------------------------------------
# Main function that builds the App
# --------------------------------------------------


class MainApp(App):
    def build(self):

        return MyBoxLayout()


if __name__ == '__main__':
    MainApp().run()
