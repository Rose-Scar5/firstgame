from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.icon = "square.jpg"
        self.title = "Hello World"
        return Label(text = "Hello world")
    
if __name__=="__main__":
    app = MyApp()
    app.run()