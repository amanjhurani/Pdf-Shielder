import re
from PIL import Image
import os
from libraries.progressBar import printProgressBar




def convertImgToPdf(wd, count, input_path):
    print("Converting Images to Pdf!!!")
    # list to store files
    res = []
    init = 1
    # folder path
    dir_path = wd + '\images\\'
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            img_name = 9+init
            res.append(Image.open("{}\{}.jpg".format(dir_path,img_name)).convert('RGB'))
        printProgressBar(init, count, prefix = 'Progress:', suffix = 'Complete', length = count)
        init += 1

    first = res[0]
    rest = res[1:]

    first.save(r"{}\{}".format(wd, input_path), save_all=True, append_images=rest)
    print("Converting Images to pdf Completed!!!")