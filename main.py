from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.scrollview import ScrollView

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from scrollLabel import ScrollLabel
from ruffier import test
from seconds import Seconds
from kivy.uix.popup import Popup


# Window.clearcolor = (1, .92, .51, 1)
btn_color = (0, 0.9, 0.64, 1)

age = 7
name = ""
p1, p2, p3 = 0, 0, 0


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


def get_result():
    res = test(p1, p2, p3, age)
    return name + '\n' + res[0] + '\n' + res[1]


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = ScrollLabel(txt_instruction)

        lbl1 = Label(text='Введите имя:', halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введите свой возраст:', halign='right')

        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global age,name
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age <7:
            age = 7
            self.in_age.text = str(age)
            popup = Popup(title="Ошибка", content = Label(text = "Возраст должен быть от 7 лет"),
                          size_hint = (None,None), size=(600,600), pos_hint={'center_x':0.5,'center_y':0.5})
            popup.open()
        else:
            self.manager.current = 'pulse1'


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = ScrollLabel(txt_test1, textcolor='#FFFFFF')
        self.lbl1 = ScrollLabel('Считайте пульс', textcolor='#FFFFFF')
        self.lbl_sec = Seconds(15, textcolor='#FFFFFF')
        self.lbl_sec.bind(done=self.sec_finished)

        line1 = BoxLayout()
        vlay = BoxLayout(orientation='vertical')
        vlay.add_widget(self.lbl1)
        vlay.add_widget(self.lbl_sec)
        line1.add_widget(instr)
        line1.add_widget(vlay)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line2.add_widget(lbl_result)
        line2.add_widget(self.in_result)

        self.btn = Button(text='Начать', pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        self.line3 = BoxLayout(size_hint = (0.8, None), height='80sp', pos_hint={'center_x':0.5})
        self.line3.add_widget(self.btn)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.line3)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True

        self.line3.remove_widget(self.btn)
        self.btn_back = Button(text='Назад')
        self.btn_back.background_color = btn_color
        self.line3.add_widget(self.btn_back)
        self.line3.add_widget(self.btn)
        self.btn_back.on_press = self.back


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'

    def back(self):
        self.manager.current = self.manager.previous()

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(txt_sits)

        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        instr = ScrollLabel(txt_test1, textcolor='#FFFFFF')
        self.lbl1 = ScrollLabel('Считайте пульс', textcolor='#FFFFFF')
        self.lbl_sec = Seconds(15, textcolor='#FFFFFF')
        self.lbl_sec.bind(done=self.sec_finished)

        line0 = BoxLayout()
        vlay = BoxLayout(orientation='vertical')
        vlay.add_widget(self.lbl1)
        vlay.add_widget(self.lbl_sec)
        line0.add_widget(instr)
        line0.add_widget(vlay)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Результат:', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result1.set_disabled(True)

        line1.add_widget(lbl_result)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Результат после оттдыха', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)
        self.in_result2.set_disabled(True)

        line2.add_widget(lbl_result)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line0)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self,instance,value):
        if value:
            if self.stage == 0:
                self.stage =1
                self.lbl1.set_text('Отдыхайте')
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.set_text("Считайте пульс")
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершить'
                self.next_screen =True
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False and p3 == False:
                p2 = 0
                self.in_result1.text = str(p2)
                p3 = 0
                self.in_result2.text = str(p3)
            elif p2 == False:
                p2 = 0
                self.in_result1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = ScrollLabel('')
        self.outer.add_widget(self.instr)

        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        self.instr.set_text(get_result())



class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartCheck()
app.run()
