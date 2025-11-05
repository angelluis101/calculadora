from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

expresion = ""  # Variable global para almacenar la expresión


class CalculadoraScreen(MDScreen):
    def press(self, numero):
        global expresion
        expresion += str(numero)
        self.ids.display.text = expresion

    def limpiar(self):
        global expresion
        expresion = ""
        self.ids.display.text = ""

    def borrar_ultimo(self):
        global expresion
        expresion = expresion[:-1]
        self.ids.display.text = expresion

    def igual(self):
        global expresion
        try:
            if expresion:
                resultado = str(eval(expresion))
                self.ids.display.text = resultado
                expresion = resultado
        except Exception:
            self.ids.display.text = "Error"
            expresion = ""


class CalculadoraApp(MDApp):
    def build(self):
        self.title = "Calculadora CBTA 131"
        self.icon = "ID2222564.png"
        return CalculadoraScreen()

    def on_start(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"


if __name__ == "__main__":
    CalculadoraApp().run()
