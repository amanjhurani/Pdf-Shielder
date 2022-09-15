# import module
from pdf2image import convert_from_path
import os
from PyPDF2 import PdfReader
from libraries.progressBar import printProgressBar


def convertPdfToImage(input_path, wd):
    # folder path
    file_path = wd + '\\' + input_path
    reader = PdfReader(file_path)

    # printProgressBar(0, len(reader.pages), prefix = 'Progress:', suffix = 'Complete', length = len(reader.pages))
    print("Start Converting PDF To Images!!!")

    dir_path = wd + '\images'
    for f in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, f))

    # Store Pdf with convert_from_path function
    images = convert_from_path(file_path, dpi=180, thread_count=3, poppler_path=r"C:\Program Files\poppler-22.04.0\Library\bin", size=(1580,2308))

    for i in range(len(images)):
        images[i].save('images/'+ str(10+i) +'.jpg', 'JPEG')
        printProgressBar(i+1, len(reader.pages), prefix = 'Progress:', suffix = 'Complete', length = len(reader.pages))
    
    print("Converting PDF To Images Completed!!!")
    return len(reader.pages)
