# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

import os
from shutil import copy2

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
    def update_website(self):

        # Recreate the postlist since passing variables around is a boner in Kivy
        postlist =os.listdir('content/home/')

        # Try to remove these non-post files
        for each in postlist:
            if each[0] == '.' or each[0]=='_':
                try:
                    postlist.remove(each)
                except:
                    pass

        # Find the file to remove
        post_to_remove = postlist[int(self.ids.rm_post_id.text)-1]
        print(post_to_remove)
        os.remove('content/home/'+post_to_remove)
        # Remove the associated static content file
        os.remove('static/img/home/'+post_to_remove[:-3])
        # Call the update_org_access_website.sh script to update the website/The Github repository
        os.system('bash update_org_access_website.sh')

        return
    pass


class AddPost(FloatLayout):

    def update_website(self):
        # This function will create a new post, based on the info in the input boxes, and then update the website/git repository
        image_name = self.ids.path_to_image.text
        post_name = self.ids.new_post_name.text
        # Convert the spaces in post_name to underscores
        post_name = post_name.replace(" ", "_")
        post_blurb = self.ids.post_blurb.text

        # Lets copy the desired image to the static/img/home directory for consistency
        # MODIFY BASED ON THE COMPUTER RUNNING THE PROGRAM
        copy2('/Users/samjett/Desktop/'+ image_name, 'static/img/home/'+post_name)

        # Lets create a new markdown file based on the minimal template below, and input the values entered in the GUI
        # +++
        # draft = false
        # image = "img/home/blu_pepper.jpg"
        # showonlyimage = true
        # date = "2018-11-20T19:50:47+05:30"
        # title = "Hoodie from Blu Pepper"
        # weight = 1
        # +++
        # Import datetime module to get current date

        from datetime import datetime

        # Open the file and fill its contents
        f = open('content/home/'+post_name+'.md', 'w+')
        f.write('+++\n')
        f.write('draft = false\n')
        f.write('image = "img/home/'+post_name+'"\n')
        f.write("showonlyimage = false\n")
        f.write('date = "'+str(datetime.now().date())+'"\n')
        f.write('Title = "'+post_name.replace('_', ' ')+'"\n')
        f.write('weight = 1\n') # All posts are written with weight 1; This can be changed if desired
        f.write('+++\n\n')
        f.write(post_blurb+ '\n\n')
        f.close()

        # The final step should just be to run the shell script to update the website, just like in the remove case
        # Call the update_org_access_website.sh script to update the website/The Github repository
        os.system('bash update_org_access_website.sh')
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
        for each in postlist:
            if each[0] == '.' or each[0]=='_':
                try:
                    postlist.remove(each)
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