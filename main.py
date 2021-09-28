#!/usr/bin/python
import sys
import os
from shutil import copyfile
from sys import exit
from pprint import pprint
from helper.font_style import text
from helper.file_helper import *


def print_welcome_script():
    print(text.BackgroundLightYellow + text.Bold + text.Black)
    print("╭────────────────────────────╮")
    print("│ 🝝                          │")
    print("│       IMAGE ANALIZER       │")
    print("│                          🝝 │")
    print("╰────────────────────────────╯")
    print(text.BackgroundDefault + text.ResetBold +
          text.default_text_color + "\n")


try:

    print_welcome_script()

    ##############################################
    # load list of images from file
    ##############################################

    image_list_file_path = "images.txt"

    imagelist = load_original_data_mass_file(image_list_file_path)

    saveList(image_list_file_path, imagelist)

    print("Image analyzer finished!\n")


except IOError as e:
    print("Unable to access file. %s" % e)
    exit(1)
except:
    print("Unexpected error:", sys.exc_info())
    exit(1)
