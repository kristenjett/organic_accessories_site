# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

import os

# This app will be run to create the Kivy frontend GUI to allow adjustments to the Organic-Accessories.com website. 
# Specifically, the GUI will allow the user to add a new post to the website, or to remove an existing post from the site.

# Load in the button styles created in the /kv folder
Builder.load_file('./kv/buttons.kv')


# Define global variables

class SelectImage(Button):
    pass

class UpdateWebsite(Button):
    pass

class RemovePost(FloatLayout):
    def select_image(self):
        print("Select image called")
        return
    def update_website(self):

        # Recreate the postlist since passing variables around is a boner in Kivy
        postlist =os.listdir('content/home/')

        # Try to remove these non-post files
        try:
            postlist.remove('_index.md')
        except:
            pass
        try:
            postlist.remove('.DS_Store')
        except:
            pass


        # Find the file to remove
        post_to_remove = postlist[int(self.ids.rm_post_id.text)-1] + '.md'
        print(post_to_remove)
        # print(self.ids.rm_post_id.text)
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
    def add_post(self):
        # Try to remove the addpost widget, if it already exists, and try to remove the removepost widget, so 
        # that the addpost screen will be created from scratch again, removing any user inputs
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
        # Try to remove the addpost widget, if it already exists, and try to remove the removepost widget, so 
        # that the removepost screen will be created from scratch again, removing any user inputs
        try:
            self.remove_widget(self.addpost)
        except:
            pass
        try:
            self.remove_widget(self.removepost)
        except:
            pass
            
        # The below section builds the list of current posts on the website from listdir in the content/home directory
        # Create the text table to include all of the posts taken from the content directory
        postlist =os.listdir('content/home/')

        post_out = ''
        counter = 1

        # Try to remove these non-post files
        try:
            postlist.remove('_index.md')
        except:
            pass
        try:
            postlist.remove('.DS_Store')
        except:
            pass

        for each in postlist:
            # Remove the .md from the end of each entry   
            new_element = str(counter)+'.) ' + each[:-3]
            new_element = new_element + ''.join([' ']*(30-len(new_element)))
            post_out = post_out+new_element
            if counter %3 == 0:
                post_out = post_out+'\n'
            counter = counter+1        
        
        self.removepost = RemovePost()
        self.removepost.ids.postlistlbl.text = post_out

        # Print the output to stdout
        print(self.removepost.ids.postlistlbl.text)
        app = App.get_running_app()
        self.add_widget(self.removepost)
        return



class MainApp(App):

    def build(self):
        self.default = DefaultState()
        self.title = 'Update Organic Accessories Website'
        return self.default

if __name__ == "__main__":
    app = MainApp()
    app.run()