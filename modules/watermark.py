from PIL import Image, ImageDraw, ImageFont
import os
import logging
from modules.mytools import MyTools

class WaterMark():
    image_name = ''

    def start(self):
        print('*** Watermark ***')
        global image_name
        image_name = None
        while image_name == None: # Make sure user enter full image path, for example: C:/My File/pic.png
            image_name = input('Enter image path:\n')
            my_tool = MyTools()
            image_name = my_tool.get_complete_path_from_file_name(image_name)
            if image_name == None:
                print('Incorrect path - No image found. \n')

        # Attributes
        self.font_size = 20
        self.x_space = 0.2  # bigger than 3? more space!
        self.y_space = 0.1
        self.sign_text = input('\nEnter text to sign:\n')

        while len(self.sign_text) == 0:
            self.sign_text = input('\nEnter text for the signature:\n')

        self.sign_now()

    def sign_now(self):
        global image_name
        base = Image.open(image_name).convert('RGBA')
        width, height = base.size

        while True:
            try:
                opacity = int(input('\nEnter text opacity from 0 to 255 (25 recommended):\n')) # From 0 to 255)
                if opacity < 0 or opacity > 255:
                    raise Exception()
                break
            except Exception as ex:
                print('Value must be from 0 to 255!')
                pass

        # Make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

        # Get a font
        fnt = ImageFont.truetype('fonts/alph.ttf', self.font_size)
        # Get a drawing context
        d = ImageDraw.Draw(txt)
        for i, y in enumerate(range(0, height, int(height*self.y_space))):
            for x in range(0, width, int(width*self.x_space)):
                d.text((x+(width*self.x_space/2)*(i%2), y), self.sign_text, font=fnt, fill=(0, 0, 0, opacity))

        out = Image.alpha_composite(base, txt)
        extension = '.png'
        print('extension is ' + extension)
        new_image_name = os.path.splitext(image_name)[0]+'-watermark' + extension
        out.save(new_image_name)
        print('New photo saved successfully!')
        print('Path: ' + new_image_name)
        out.show()
        input('\nPress any key to continue . . .')
        print('###########\n\n')
