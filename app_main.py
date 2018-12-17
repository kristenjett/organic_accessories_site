from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder

# Load in the button styles created in the /kv folder
Builder.load_file('./kv/buttons.kv')
class SelectImage(Button):
    pass


class UpdateWebsite(Button):
    pass

class RemovePost(FloatLayout):
    def select_image(self):
        print("Select image called")
        return
    def update_website(self):
        print("Update Website called")
        return
    pass


class AddPost(FloatLayout):
    def select_image(self):
        print("Select image called")
        return
    def update_website(self):
        print("Update Website called")
        return
    pass

class DefaultState(FloatLayout):
    # Defines functions to be called by the two buttons in default state
    def select_image(self):
        print("Select image called")
        return
    def update_website(self):
        print("Update Website called")
        return
    def add_post(self):
        try:
            self.remove_widget(AddPost())
        except:
            pass
        try:
            self.remove_widget(RemovePost())
        except:
            pass
        self.add_widget(AddPost())

    def remove_post(self):
        try:
            self.remove_widget(AddPost())
        except:
            pass
        try:
            self.remove_widget(RemovePost())
        except:
            pass
        self.widget = RemovePost()
        self.add_widget(RemovePost())
        return



class MainApp(App):

    def build(self):
        self.widget = DefaultState()
        self.title = 'Update Organic Accessories Website'
        return DefaultState()

if __name__ == "__main__":
    app = MainApp()
    app.run()