import os
from pdf2image import convert_from_path, convert_from_bytes
from os import path
from glob import glob
from wand.image import Image
from modules.mytools import MyTools

class ConvertPNG:
    png_name = ''
    format = 'pdf'
    def __init__(self):
        global png_name
        # Attributes
        print('*** Convert PNG to PDF ***')

        png_name = None
        while png_name == None:  # Make sure user enter full file path, for example: C:/My File/pic.png
            png_name = input('Enter PNG path:\n')
            png_name = MyTools().get_complete_path_from_file_name(png_name, 'png')
            if png_name == None:
                print('Incorrect path - No PNG found. \n')

        self.convertNow()

    def convertNow(self):
        global png_name
        counter = 1
        my_path = os.path.dirname(png_name)
        with Image(filename=png_name) as img:

            with img.convert('pdf') as converted:
                save_file_name = f"{my_path}\\page-{counter}.pdf"
                while os.path.isfile(save_file_name):
                    print(counter)
                    counter += 1
                    save_file_name = f"{my_path}\\page-{counter}.pdf"

                converted.save(filename=save_file_name)
                print(f'Done successfully! \nPDF Saved to: {my_path}')
                input('\nPress any key to continue . . .')
