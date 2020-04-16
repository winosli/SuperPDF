import os

from PIL import Image
from modules.mytools import MyTools
from time import gmtime, strftime

class Compress:
    counter = 1
    save_path = 2
    save_option = '3'

    def __init__(self):
        self.curr_date_for_path = strftime("%Y-%m-%d %H_%M_%S",
                                      gmtime())  # We are creating unique file name to save all JPEGs files if needed (option 3).

    def change_now(self, image_path, filename, extension):
        global curr_date_for_path
        full_path = image_path + "//" + filename # Full path with imagename
        global save_option
        global counter
        img = Image.open(full_path).convert('RGB')

        while os.path.exists((str(self.counter) + ".jpg")):
            counter += 1

        #while save_to_path != 1 or save_to_path != 2
        if save_option == '3': # Save to a new path with same names
            self.counter += 1
            image_path += "//" + self.curr_date_for_path
            if not os.path.exists(image_path):  # File is not exist - but check to make sure!
                os.makedirs(image_path)  # We are going to save all pictures from PDF in this new folder
            new_image_name = image_path + f"//{filename}" + "." + f"{extension}".replace(".","")
            extension = str(extension).upper().replace(".","")
            if extension == "JPG":
                extension = "JPEG"
            img.save(new_image_name, str(extension).upper().replace(".",""), optimize=True,quality=80)
            self.success_print(new_image_name)

        elif save_option == '1': # Override original images
            save_path = full_path + "//" + full_path
            img.save(save_path,optimize=True, quality=80)
            self.success_print(full_path)
        else: # Copy but keep both files
            #save_path = image_name.replace('.jpg','-compress.jpg').replace('.png','-compress.png').replace('.JPEG','-compress.JPEG')
            save_path = image_path + "//compress-" + filename
            img.save(save_path)
            self.success_print(full_path)

    def success_print(self, filename):
        print(f'Done successfully! {filename} is created!\n')

    def start(self):
        global save_option
        print('*** Compress Images ***')
        image_path = input('Enter images path:\n')
        if not os.path.exists(image_path):
            print('Path is not exist! \n')
            self.start()

        #image_name = 'ss2'
        #image_path = image_name

        if '\\' in image_path: # this is a path from other place - ask user when he want to save the picture
            save_option = input('Save Compress images to: \n[1] Override original images \n[2] Copy but keep both files \n[3] New path with same names\n')

        for filename in os.listdir(image_path):
            currect_path = MyTools().get_complete_path_from_file_name_for_pictures(image_path + "//" + filename)
            if currect_path != None:
                filename = MyTools().get_file_name_from_full_path(currect_path)
                extension = MyTools().get_file_extension(currect_path)
                self.change_now(image_path, filename, extension)