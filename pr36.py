from binascii import a2b_hex
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<AuthScreen>:
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            hint_text: 'Логин'
        TextInput:
            hint_text: 'Пароль'
        BoxLayout:
            CheckBox:
                on_active:
                    root.btn_click()
            Label:
                text: 'Запомнить пароль'
        Button:
            text: 'Авторизоваться'
        Button:
            text: 'Перейти к регистрации'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'register'
        Label:
            text: 'Забыли пароль?'
            on_touch_down:
                root.btn_click()

<RegisterScreen>:
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            hint_text: 'Имя'
        TextInput:
            hint_text: 'Фамилия'
        TextInput:
            hint_text: 'Логин'
        TextInput:
            hint_text: 'Пароль'
        TextInput:
            hint_text: 'Повтор пароля'
        Button:
            text: 'Зарегистрироваться'
        Button:
            text: 'Вернуться к авторизации'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'auth'
""")

# Declare both screens
class AuthScreen(Screen):
    def btn_click(self):
        print(self)

class RegisterScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(AuthScreen(name='auth'))
        sm.add_widget(RegisterScreen(name='register'))

        return sm

if __name__ == '__main__':
    MyApp().run()