from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label


class Taskbar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        dropdown1 = DropDown()
        dropdown1.add_widget(Button(text='Option 1'))
        dropdown1.add_widget(Button(text='Option 2'))
        
        dropdown2 = DropDown()
        dropdown2.add_widget(Button(text='Option 3'))
        dropdown2.add_widget(Button(text='Option 4'))
        
        button1 = Button(text='Dropdown 1')
        button1.bind(on_release=dropdown1.open)
        self.add_widget(button1)
        
        button2 = Button(text='Dropdown 2')
        button2.bind(on_release=dropdown2.open)
        self.add_widget(button2)


class LeftWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        button1 = Button(text='Button 1')
        self.add_widget(button1)
        
        button2 = Button(text='Button 2')
        self.add_widget(button2)
        
        dropdown = DropDown()
        dropdown.add_widget(Button(text='Option 1'))
        dropdown.add_widget(Button(text='Option 2'))
        
        button3 = Button(text='Dropdown')
        button3.bind(on_release=dropdown.open)
        self.add_widget(button3)


class CenterWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.add_widget(Label(text='Center Widget', font_size=30))


class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        
        taskbar = Taskbar(orientation='horizontal', size_hint=(1, 0.1))
        root.add_widget(taskbar)
        
        main_widget = BoxLayout(orientation='horizontal')
        root.add_widget(main_widget)
        
        left_widget = LeftWidget(orientation='vertical', size_hint=(0.3, 1))
        main_widget.add_widget(left_widget)
        
        center_widget = CenterWidget(orientation='vertical', size_hint=(0.7, 1))
        main_widget.add_widget(center_widget)

        return root


if __name__ == '__main__':
    MyApp().run()
