from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np



import os
from libraries.progressBar import printProgressBar



def applyWatermark(wd, overlay_path):
    print("Applying Watermark to Images!!!")
    # list to store files
    res = []
    init = 0
    # folder path
    dir_path = wd + '\images\\'
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            image = Image.open("{}/{}".format(dir_path,path))
            watermark_image = image.copy()
            logo = Image.open('{}/{}'.format(wd,overlay_path))
            watermark_image.paste(logo, (0, 0), mask = logo)
            watermark_image.save("{}/{}".format(dir_path,path), 'JPEG')

    print("Applying Watermark to images completed.")


