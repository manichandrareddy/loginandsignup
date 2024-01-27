Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from kivy.app import App
... from kivy.uix.button import Button
... from kivy.uix.boxlayout import BoxLayout
... 
... # Assuming 'firebase_admin' is used for Firebase authentication in Python
... import firebase_admin
... from firebase_admin import auth
... from kivy.clock import mainthread
... 
... class OrderDetailsApp(App):
...     def build(self):
...         layout = BoxLayout(orientation='vertical')
...         self.combo_btn = Button(text='Combo')
...         self.home_btn = Button(text='Home')
...         self.combo_btn.bind(on_press=self.on_combo_pressed)
...         self.home_btn.bind(on_press=self.on_home_pressed)
...         layout.add_widget(self.combo_btn)
...         layout.add_widget(self.home_btn)
...         return layout
... 
...     def logout(self):
...         # Assuming Firebase Admin SDK is initialized elsewhere
...         auth.current_user = None
...         # Transition to the login screen would be handled here
...         print("Logged out, proceed to login screen")
... 
...     def on_combo_pressed(self, instance):
...         # Transition to the Combo screen would be handled here
...         print("Combo button pressed, proceed to Combo screen")
... 
...     def on_home_pressed(self, instance):
...         # Transition to the Home screen would be handled here
...         print("Home button pressed, proceed to Home screen")
... 
... if __name__ == '__main__':
...     OrderDetailsApp().run()
...  note
... 
