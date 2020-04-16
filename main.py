import os

import PyPDF2
import sys
from modules.mergepdf import MergePDF
from modules.changeresolution import ChangeResolution
from modules.watermark import WaterMark
from modules.convertpdf import ConvertPDF
from modules.convertpng import ConvertPNG
from modules.convertpngtojpeg import ConvertPNG_ToJPEG
from modules.compress import Compress
from modules.mytools import MyTools
class Main:

    def start(self):
        print('\nWelcome to Super PDF\n')
        all_options = ['[1] Merge PDFs','[2] Watermark PDF', '[3] Convert PDF to PNG','[4] Convert PNG to PDF','[5] Convert PNG to JPEG', '[6] Compress Multiple images','[7] Rename Multiple images','[8] Change image resolution']
        for option in all_options:
            print(option)

        print('\nSelect an option to begin:')

        inp = input('')
        if inp == '1':
            MergePDF().start()
        elif inp == '2':
            WaterMark().start()
        elif inp == '3':
            ConvertPDF().start()
        elif inp == '4':
            ConvertPNG().start()
        elif inp == '5':
            ConvertPNG_ToJPEG().start()
        elif inp == '6':
            Compress().start()
        elif inp == '7':
            target_path = input('*** Rename Multiple images ***\nInsert full path of target folder: \n')
            new_image_name = input('Optional: Insert new image name (by default it\'s numbers only): ')
            i = 0
            for filename in os.listdir(target_path):
                file_format = None
                images_format = ['.jpg','.png','.jpeg']
                for frmt in images_format:
                    if frmt in filename:
                        file_format = frmt

                if file_format != None:
                    os.rename(target_path + '/' + filename, target_path + '/' + new_image_name + str(i) + '.jpg')
                    i = i + 1
            print(f'Done successfully! \nSaved to: ' + target_path)
            input('\nPress any key to continue . . .')
        elif inp == '8':
            ChangeResolution().start()
        else:
            print('Option is not exist yet - we are working on it.')

    def __init__(self):
        self.start()

while(True):
    main = Main()
