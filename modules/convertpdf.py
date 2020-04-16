import os
from wand.image import Image
from modules.mytools import MyTools
from time import gmtime, strftime

class ConvertPDF:
    pdf_name = ''
    format = 'png'

    def start(self):
        global pdf_name
        # Attributes
        print('*** Convert PDF to PNG ***')

        pdf_name = None
        while pdf_name == None:  # Make sure user enter full file path, for example: C:/My File/pic.pdf
            pdf_name = input('Enter PDF path:\n')
            pdf_name = MyTools().get_complete_path_from_file_name(pdf_name, 'pdf')
            if pdf_name == None:
                print('Incorrect path - No PDF found. \n')

        self.convertNow()

    def convertNow(self):
        global pdf_name
        curr_date_for_path = strftime("%Y-%m-%d %H_%M_%S", gmtime())
        my_path = os.path.dirname(pdf_name)
        save_path = my_path + "\\" + curr_date_for_path
        if not os.path.exists(save_path): # File is not exist - but check to make sure!
            os.makedirs(save_path) # We are going to save all pictures from PDF in this new folder

        with Image(filename=pdf_name) as img:
            with img.convert('png') as converted:
                converted.save(filename=save_path + "\\page.png")
                print(f'Done successfully!\n{len(img.sequence)} Photos Saved to: {save_path}')
                input('\nPress any key to continue . . .')
                print('###########\n\n')
