import sys
import os
from PIL import Image, UnidentifiedImageError
from time import gmtime, strftime

class ConvertPNG_ToJPEG:
    from_file = ''
    to_file = ''
    all_png = ''

    def start(self):
        global all_png
        global from_file
        global to_file
        print('*** PNG to JPEG ***')
        while(True):
            try:
                from_file = input('Insert folder that contain ALL PNG files: \n')
                if not os.path.exists(from_file):
                    print('Path is not exist!\n')
                    continue
                #to_file = input('Insert target file to save all JPEGS: ')
                break
            except IndexError:
                print('Insert From file (PNG pictures) and To File (JPEG pictures):\n')

        curr_date_for_path = strftime("%Y-%m-%d %H_%M_%S", gmtime()) # We are creating unique file name to save all JPEGs files
        to_file = from_file + "\\" + curr_date_for_path

        if not os.path.exists(to_file):  # File is not exist - but check to make sure!
            os.makedirs(to_file)  # We are going to save all pictures from PDF in this new folder

        try:
            all_png = os.listdir(from_file)
            self.convertPNGtoJPEG()
        except UnidentifiedImageError as ex:
            print('ERROR! Your folder must contain PNG files only!\n')
            self.start()
        except FileNotFoundError as ex_not_found:
            print('ERROR! Wrong paths!\n')
            self.start()
        # except OSError as syntax_error:
        #     print('Syntax Error occur (Conversion not complete), Try to close your target file and try again: ' + str(syntax_error))
        #     self.start()


    def convertPNGtoJPEG(self):
        global all_png
        global from_file
        global to_file
        counter = 0
        for pic_name in all_png:
            if '.png' in pic_name:
                counter += 1
                with Image.open(from_file + "/" + pic_name) as new_pic:
                    rgb_img = new_pic.convert('RGB')
                    if ':' in to_file:
                        # In this case this is a full path
                        rgb_img.save(to_file + "/" + pic_name.replace(".png", ".jpeg"),
                                     'jpeg')  # you can convert to PNG even if that was jpeg
                    else:
                        rgb_img.save(to_file + "/" + pic_name.replace(".png",".jpeg")) # you can convert to PNG even if that was jpeg


        print(f'Done successfully!\n{counter} pictures saved to: {to_file} folder')
        input('\nPress any key to continue . . .')