import pyqrcode
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class QRCoder(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.input = TextInput(
                        multiline=False,
                        text="Podaj nazwę strony: ",
                        padding_y=(20, 20),
                        padding_x=(50, 50),
                        size_hint=(1, 0.5)
                        )
        self.filename = TextInput(
                        multiline=False,
                        text="Podaj nazwę pliku z rozszerzeniem: ",
                        padding_y=(20, 20),
                        padding_x=(50, 50),
                        size_hint=(1, 0.5)
                        )
        self.window.add_widget(self.input)
        self.window.add_widget(self.filename)
        self.button = Button(
                        text="Stwórz kod QR",
                        size_hint=(1, 0.3),
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, e):
        pyqrcode.create(self.input)
        image = self.filename.save(self.filename)
        opener = image.open(image)
        opener.show()


if __name__ == '__main__':
    QRCoder().run()






