import re
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty, BooleanProperty
from database import Database


db= Database()
class ContentNavigationDrawer(MDScrollView):
    access_denied = BooleanProperty(True)
    screen_manager= ObjectProperty()
    nav_drawer= ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
         
class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class LogoutScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class RegistrationScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
            
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette= "DeepOrange"
        #self.content_navigation_drawer = ContentNavigationDrawer(screen_manager=self.screen_manager, nav_drawer=self.nav_drawer)
        
    def login(self, username, password):
        user= db.login(username.text, password.text)
        if user:
            username.text= ""
            password.text= ""
            #self.content_navigation_drawer.access_denied = False
            self.root.ids['screen_manager'].current= 'home'
            #print("User is logged in successfully")
        else:
            print("You have entered invalid credentials")
            
    def register(self, username, email, firstname, lastname, password, confirm_password):
        if password.text != confirm_password.text:
            print("Both passwords should be the same!!")
            return 
        if not username.text or not email.text:
            print("The email and username are required !!")
            return 
        if not self.is_valid_email(email.text):
            print("Your email is not valid")
            return 
        db.create_user(username.text, email.text, password.text)
        username.text= ""
        email.text= ""
        firstname.text= ""
        lastname.text= ""
        password.text= ""
        confirm_password.text= ""
        self.root.ids['screen_manager'].current= 'login'
        #print("You are successfully registered")
    
    def is_valid_email(self, email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email)
    def on_stop(self):
        db.close_connection()
            
    
if __name__ == "__main__":
    Window.size = (360, 640)
    app= MainApp()
    app.run()