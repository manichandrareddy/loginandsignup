Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup

# Assuming Firebase for Python is set up and firebase_auth is an instance of the authentication service
from firebase_admin import auth as firebase_auth

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login_user)
        self.add_widget(self.login_button)

        self.create_account_label = Label(text='Create Account')
        self.create_account_label.bind(on_touch_down=self.create_account)
        self.add_widget(self.create_account_label)

        self.progress_bar = ProgressBar(max=100)
        self.add_widget(self.progress_bar)

    def login_user(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if not email:
            popup = Popup(title='Error', content=Label(text='Email is Required.'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return

        if not password:
            popup = Popup(title='Error', content=Label(text='Password is Required.'), size_hint=(None, None), size=(400, 400))
...             popup.open()
...             return
... 
...         self.progress_bar.value = 50  # Just to show progress, not actual loading
... 
...         try:
...             user = firebase_auth.sign_in_with_email_and_password(email, password)
...             # Assuming there's a function to handle successful login
...             self.handle_successful_login(user)
...         except firebase_auth.AuthError as e:
...             popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(400, 400))
...             popup.open()
...         finally:
...             self.progress_bar.value = 0
... 
...     def create_account(self, instance, touch):
...         # Assuming there's a function to switch to the registration screen
...         self.switch_to_registration()
... 
...     def handle_successful_login(self, user):
...         # Logic to handle successful login
...         pass
... 
...     def switch_to_registration(self):
...         # Logic to switch to the registration screen
...         pass
... 
... class LoginApp(App):
...     def build(self):
...         return LoginScreen()
... 
... if __name__ == '__main__':
...     LoginApp().run()
...  note
... 
