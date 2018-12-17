from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

import os

# Load in the button styles created in the /kv folder
Builder.load_file('./kv/buttons.kv')


# Define global variables
global post_list
global path_to_file
global new_post_name
global new_post_blurb

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

    def update_website(self):
        app = App.get_running_app()
        print("Update Website called")
        print("The name of the new post is " + app.)
        return
    pass

class DefaultState(FloatLayout):
    # Defines functions to be called by the two buttons in default state
    def update_website(self):
        print("Update Website called")
        return
    def add_post(self):
        try:
            self.remove_widget(self.addpost)
        except:
            pass
        try:
            self.remove_widget(self.removepost)
        except:
            pass
        self.addpost = AddPost()
        self.add_widget(self.addpost)

    def remove_post(self):
        try:
            self.remove_widget(self.addpost)
        except:
            pass
        try:
            self.remove_widget(self.removepost)
        except:
            pass
        
        self.removepost = RemovePost()
        app = App.get_running_app()

        # Get the current post list from the content/home folder
        app.post_list = os.listdir('content/home')

        # Remove the .DS_Store and _index files
        try:
            app.post_list.remove('_index.md')
            app.post_list.remove('.DS_Store')
        except:
            pass

        # Turn the current posts on the site into a single string
        post_str = ""
        counter = 1
        for post in app.post_list:
            post_str = post_str + str(counter)+' - '
            post_str = post_str + post[:-3]
            if counter < len(app.post_list):
                post_str = post_str + '   |   '
                counter = counter+1

        self.removepost.ids.postlistlbl.text = post_str

        self.add_widget(self.removepost)
        return



class MainApp(App):
    # Define the app attributes that I will use and modify as the app is running
    post_list = []
    path_to_image = ""
    new_post_name = ""
    post_blurb = ""
    rm_post_id=''

    def build(self):
        self.default = DefaultState()
        self.title = 'Update Organic Accessories Website'
        return self.default

if __name__ == "__main__":
    app = MainApp()
    app.run()