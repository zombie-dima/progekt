# программа с двумя экранами
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
class ScrButton(Button):
    def __init__(self,screen,direction = 'right',goal ='main',**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation = 'vertical',padding =8,spacing = 8)
        h1 = BoxLayout()
        txt = Label(text = 'Выбери экран')

        v1.add_widget(ScrButton(self,direction='left',goal='first',text='1'))
        v1.add_widget(ScrButton(self,direction='right',goal='second',text='2'))
        v1.add_widget(ScrButton(self, direction='down', goal='third', text='3'))
        v1.add_widget(ScrButton(self, direction='up', goal='fourth', text='4'))

        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        v1 = BoxLayout(orientation = 'vertical', size_hint =(.5,.5), pos_hint={'center_x': 0.5,'center_y':0.5})
        btn = Button(text = 'Выбор 1', size_hint = (.5,1), pos_hint = {'left':0})
        btn_back = ScrButton(self,direction='right',goal ='main',text = "Назад", size_hint=(.5,1), pos_hint={'right':1})
        v1.add_widget(btn)
        v1.add_widget(btn_back)
        self.add_widget(v1)

class SecondScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        v1 = BoxLayout(orientation = 'vertical')

        h1_0 = BoxLayout(size_hint = (0.8,None), height = '30sp')
        h1_0.add_widget((Label(text='Введите пароль', halign = 'right')))
        self.input = TextInput(multiline = False)
        v1.add_widget(h1_0)

        h1 = BoxLayout()
        self.txt = Label(text = 'Выбор:2')
        btn_false = Button(text = 'OK!')
        btn_back = ScrButton(self, direction='left',goal = 'main', text = "Назад")
        v1.add_widget(self.txt)
        h1.add_widget(btn_false)
        h1.add_widget(btn_back)
        v1.add_widget(h1)
        self.add_widget(v1)
        btn_false.on_press = self.change_text


    def change_text(self):
        self.txt.text = self.input.text + '?Не сработало ...'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main'))
        sm.add_widget(FirstScreen(name = 'first'))
        sm.add_widget(SecondScr(name='second'))
        return sm
app = MyApp()
app.run()