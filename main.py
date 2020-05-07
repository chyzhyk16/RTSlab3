from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import time

import lab3_1
import lab3_2
import lab3_3


class MainApp(App):

    def on_press_button1(self):
        try:
            n = int(App.get_running_app().ti1.text)
            result=lab3_1.calc1(n)
            App.get_running_app().lb1.text = result[0]
            layout = GridLayout(cols=1, padding=10)

            popupLabel = Label(text=str(result[1]))
            closeButton = Button(text="Close")

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)
            popup = Popup(title='Time',
                          content=layout,
                          size_hint=(None, None), size=(200, 200))
            popup.open()
            closeButton.bind(on_press=popup.dismiss)

        except:
            App.get_running_app().lb1.text = 'Некоректний ввід'
            return None

    def on_press_button2(self):

        try:
            learning_rate = float(App.get_running_app().ti2.text)
            maxtime = float(App.get_running_app().ti3.text)
            maxiter = int(App.get_running_app().ti4.text)
            App.get_running_app().lb2.text = lab3_2.calc2(learning_rate, maxtime, maxiter)
        except:
            App.get_running_app().lb2.text = 'Некоректний ввід'
            return None

        return None

    def on_press_button3(self):
        try:
            kofstr = str(App.get_running_app().ti5.text)
            kof = kofstr.split(',')
            y = int(App.get_running_app().ti6.text)
            t = lab3_3.calc3(int(kof[0]), int(kof[1]), int(kof[2]), int(kof[3]), y, int(kof[4]))
            App.get_running_app().lb3.text = str(t)
        except:
            App.get_running_app().lb3.text = 'Некоректний ввід'
            return None

        return None

    # Lab 3.1
    ti1 = TextInput(text="Input here number for factorization")
    lb1 = Label(text="Hello! Its Lab#3.1. Results will be here.")
    bt1 = Button(text="Calculate")
    bt1.bind(on_press=on_press_button1)
    res = 'empty'
    # Lab 3.2
    lb2 = Label(text="Hello! Its Lab#3.2. Weights will be here.")
    ti2 = TextInput(text="Input here learning rate")
    ti3 = TextInput(text="Input here deadline in seconds")
    ti4 = TextInput(text="Input here number of iterations")
    bt2 = Button(text="Calculate")
    bt2.bind(on_press=on_press_button2)
    # Lab 3.2
    lb3 = Label(text="Hello! Its Lab#3.3. Results will be here.")
    ti5 = TextInput(text="Input here a,b,c,d and mutation rate")
    ti6 = TextInput(text="Input here y")
    bt3 = Button(text="Calculate")
    bt3.bind(on_press=on_press_button3)

    def build(self):
        bl1 = BoxLayout(orientation='vertical')

        bl1_1 = BoxLayout(padding=20, spacing=20)

        bl1_1_1 = BoxLayout(spacing=20, orientation='vertical')
        bl1_1_1.add_widget(self.lb1)

        bl1_1.add_widget(bl1_1_1)
        bl1_1.add_widget(self.ti1)
        bl1_1.add_widget(self.bt1)

        bl1_2 = BoxLayout(padding=20, spacing=20)

        bl1_2_1 = BoxLayout(spacing=20, orientation='vertical')
        bl1_2_1.add_widget(self.lb2)

        bl1_2.add_widget(bl1_2_1)

        bl1_2_2 = BoxLayout(spacing=20, orientation='vertical')
        bl1_2_2.add_widget(self.ti2)
        bl1_2_2.add_widget(self.ti3)
        bl1_2_2.add_widget(self.ti4)

        bl1_2.add_widget(bl1_2_2)
        bl1_2.add_widget(self.bt2)

        bl1_3 = BoxLayout(padding=20, spacing=20)

        bl1_3_1 = BoxLayout(spacing=20, orientation='vertical')
        bl1_3_1.add_widget(self.lb3)

        bl1_3.add_widget(bl1_3_1)

        bl1_3_2 = BoxLayout(spacing=20, orientation='vertical')
        bl1_3_2.add_widget(self.ti5)
        bl1_3_2.add_widget(self.ti6)

        bl1_3.add_widget(bl1_3_2)
        bl1_3.add_widget(self.bt3)
        bl1.add_widget(bl1_1)
        bl1.add_widget(bl1_2)
        bl1.add_widget(bl1_3)

        return bl1


if __name__ == '__main__':
    app = MainApp()
    app.run()
