import os

from PIL import Image
from modules.mytools import MyTools

class ChangeResolution:
    is_continue = True
    counter = 1
    save_path = 2
    def change_now(self, full_image_path):
        im = Image.open(full_image_path).convert('RGB')

        try:
            x = int(input('Insert X pixels '))
            y = int(input('Insert Y pixels '))
        except ValueError as ex:
            print('Enter numbers only! ')
            return
        if x < 1 or y < 1:
            print('X and Y must be greater than 0!')
            return
        if x > 10000 or y > 10000:
            print('X and Y must be smaller than 10,001!')
            return
        img = im.resize((x, y), Image.ANTIALIAS)
        while os.path.exists((str(self.counter) + ".jpg")):
            self.counter += 1

        save_option = '3'
        print('full_image_path:',full_image_path)
        if '\\' in full_image_path: # this is a path from other place - ask user when he want to save the picture
            save_option = input('\nSave to: \n[1] Override original image \n[2] Copy but keep both files \n')
        #while save_to_path != 1 or save_to_path != 2

        if save_option == '1':
            save_path = full_image_path
            img.save(save_path)
            self.success_print(full_image_path)
        else:
            save_path = full_image_path.replace('.jpg','-copy.jpg').replace('.png','-copy.png').replace('.JPEG','-copy.JPEG')
            print('save path is',save_path)
            img.save(save_path)
            self.success_print(full_image_path)

        print(f'Done successfully!\npicture saved to: {save_path} folder')
        input('\nPress any key to continue . . .')

    def success_print(self, filename):
        print(f'Success! {filename}.jpg is created!\n')

    def start(self):
        print('*** Change image resolution ***')
        image_path = input('Enter image path:\n')
        full_image_path = MyTools().get_complete_path_from_file_name_for_pictures(image_path)
        if full_image_path != None:
            self.change_now(full_image_path)
        else:
            print(
                'Your image \'' + str(image_path) + "\' is not exist!\n")
            self.start()


