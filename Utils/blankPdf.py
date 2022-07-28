import os
from pathlib import Path
from PyPDF2 import PdfFileWriter
from Utils.createFolder import create_major_folder


def create_blank_pdf(file):
    filename = os.path.basename(file)
    filename = filename.split(".")
    filename = filename[0]
    pdf_writer = PdfFileWriter()
    x = create_major_folder()
    path = os.path.join(x, filename+"_.pdf")
    with Path(path).open(mode="wb") as output_file:
        pdf_writer.write(output_file)
    return path
