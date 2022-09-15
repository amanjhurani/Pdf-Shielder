from PyPDF2 import PdfFileReader, PdfFileWriter

def encryptPdf(wd,input_path, password):
    print("Start Locking Pdf!!!")
    with open("{}/{}".format(wd,input_path), "rb") as in_file:
        input_pdf = PdfFileReader(in_file)

        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(input_pdf)
        output_pdf.encrypt(password)
        with open("{}/password-{}".format(wd, input_path), "wb") as out_file:
            output_pdf.write(out_file)
    print("Completed Locking Pdf!!!")