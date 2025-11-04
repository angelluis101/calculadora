from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.core.image import Image as CoreImage





expresion = ""


class CalculadoraScreen(MDScreen):
    def __init__(self):
        super().__init__()
        self.crear_interfaz()
    
    def press(self, numero):
        global expresion
        expresion += str(numero)
        self.display.text = expresion
    
    def limpiar(self, *args):
        global expresion
        expresion = ""
        self.display.text = ""
    
    def borrar_ultimo(self, *args):
        global expresion
        expresion = expresion[:-1]
        self.display.text = expresion
    
    def igual(self, *args):
        global expresion
        try:
            if expresion:
                resultado = str(eval(expresion))
                self.display.text = resultado
                expresion = resultado
        except Exception:
            self.display.text = "Error"
            expresion = ""
    
    def crear_interfaz(self):
                 
        color_boton = [0.0, 0.5, 0.0, 1]         
        color_boton_operadores = [0.7, 0.7, 0.7, 1] 
       

        layout_principal = MDBoxLayout(
        orientation="vertical",
        padding=dp(20),
        spacing=dp(10),
        md_bg_color=[0.7, 1, 0, 1]  
     )


        self.display = MDTextField(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=dp(30),
            size_hint_y=0.15,
            height=dp(60),
            radius=[20, 20, 20, 20],
            line_color_normal=[0.5,0.5,0.5,1],
            line_color_focus=[0.5,0.5,0.5,1],
            fill_color_normal=[1,1,1,1],     
            fill_color_focus=[1,1,1,1],     
            mode="fill",
            text_color_normal=[0,0,0,1],    
            text_color_focus=[0,0,0,1],   
            padding=[20,10,20,10],
        )
        layout_principal.add_widget(self.display)

        botones_grid = GridLayout(
            cols=4,
            spacing=dp(10),
            size_hint_y=None,
            height=dp(360)
        )

        def crear_boton(texto, color, callback):
         return MDRaisedButton(
         text=texto,
         font_size=dp(20),
         size_hint=(1, 1),
         md_bg_color=color,
         
         on_release=callback,
         
    )


        botones = [
            ("7", color_boton), ("8", color_boton), ("9", color_boton), ("+", color_boton_operadores),
            ("4", color_boton), ("5", color_boton), ("6", color_boton), ("-", color_boton_operadores),
            ("1", color_boton), ("2", color_boton), ("3", color_boton), ("*", color_boton_operadores),
            ("<-", color_boton_operadores),("0", color_boton), ("=", color_boton_operadores), ("C", color_boton_operadores)
           
        ]

        for texto, color in botones:
            if texto == "=":
                btn = crear_boton(texto, color, self.igual)
            elif texto == "C":
                btn = crear_boton(texto, color, self.limpiar)
            elif texto == "<-":
                btn = crear_boton(texto, color, self.borrar_ultimo)
            else:
                btn = crear_boton(texto, color, lambda x, t=texto: self.press(t))
            botones_grid.add_widget(btn)

        layout_principal.add_widget(botones_grid)
        self.add_widget(layout_principal)

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
