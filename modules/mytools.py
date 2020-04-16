import time
from os.path import splitext
import os

class MyTools:

    # Use this function if you would like to get full path when user enter file without extension.
    def get_complete_path_from_file_name(self, full_path): # Full path must be include file name, for example: C:\Users\My Picture
        if full_path.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            if os.path.isfile(full_path): # File exist
                return full_path
        else:
            # Extention is not exist. Start by checking each one of them.
            my_extentions = ['.png', '.jpg', '.jpeg', '.pdf'] # You can add more potential extensions if needed!
            for extention in my_extentions:
                temp_path = full_path + extention
                if os.path.isfile(temp_path):  # File exist
                    return temp_path

    # This is for pictures only
    def get_complete_path_from_file_name_for_pictures(self, full_path): # Full path must be include file name, for example: C:\Users\My Picture
        if full_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            if os.path.isfile(full_path): # File exist
                return full_path
        else:
            # Extention is not exist. Start by checking each one of them.
            my_extentions = ['.png', '.jpg', '.jpeg', '.pdf'] # You can add more potential extensions if needed!
            for extention in my_extentions:
                temp_path = full_path + extention
                if os.path.isfile(temp_path):  # File exist
                    return temp_path

    def get_complete_path_from_file_name(self, full_path, specific_extention): # Full path must be include file name, for example: C:\Users\My Picture
        if specific_extention.startswith('.') == False: # Make sure extension start with '.'
            specific_extention = '.' + specific_extention
        if full_path.lower().endswith((specific_extention)):
            if os.path.isfile(full_path): # File exist
                return full_path
        else:
            # Extention is not exist. Start by checking each one of them.
            my_extentions = [specific_extention] # You can add more potential extensions if needed!
            for extention in my_extentions:
                temp_path = full_path + extention
                if os.path.isfile(temp_path):  # File exist
                    return temp_path

    def small_delay(self):
        print('################')
        time.sleep(3)  # Delay for last message.

    def get_path_only_without_file_name(self, full_path):
        return os.path.split(os.path.abspath(full_path))

    def get_file_extension(self, full_path):
        file_name, extension = splitext(full_path)
        return extension

    def get_file_name_from_full_path(self, full_path):
        return os.path.basename(full_path)