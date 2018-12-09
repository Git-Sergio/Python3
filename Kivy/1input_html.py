from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

class MyApp(App):
  def build(self):

    return CodeInput(lexer = HtmlLexer())

    return Button(text = "Knopka!",
      font_size = 30,
      on_press = self.btn_press,
      background_color = [1.48, .79, .4, 1],
      background_normal = '' )

  def btn_press(self, instance):
    print("Knopka Natysnuta!")
    instance.text = "Ja natysnuta"

if __name__ == "__main__":
  MyApp().run()
