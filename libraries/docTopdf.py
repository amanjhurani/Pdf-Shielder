from docx2pdf import convert
import os

def convertDocxToPdf(input_path, output_path, wd):
    print(wd+input_path, wd+output_path)
    print("Coverting Docx to PDF")
    convert(wd+input_path, wd+output_path)
    print("Docx to PDF Conversion Completed!!!")
