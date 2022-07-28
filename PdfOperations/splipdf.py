import os
from re import A
from PyPDF2 import PdfFileWriter, PdfFileReader

from Utils.createFolder import create_splitpdf_folder


def split_pdf(st,filename, pages):
    x1=create_splitpdf_folder()
    filez = os.path.basename(filename)
    filez= filez.split(".")
    filez = filez[0]
    pdf_reader = PdfFileReader(open(filename, "rb"), strict=False)
    x = 0
    y = 0
    x = int(pages[0])-1
    if len(pages)>1:
        y = int(pages[2])-1
    if y != 0:
        if x > 0:
            pdf_writer = PdfFileWriter()
            for page in range(0, x):
                pdf_writer.addPage(pdf_reader.getPage(page))
            path = os.path.join(x1, filez+"_part1.pdf")
            with open(path, 'wb') as file:
                pdf_writer.write(file)

        if y < pdf_reader.getNumPages():

            pdf_writer = PdfFileWriter()
            for page in range(y+1, pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
            path = os.path.join(x1, filez+"_part3.pdf")
            with open(path, 'wb') as file:
                pdf_writer.write(file)

        pdf_writer = PdfFileWriter()
        for page in range(x, y+1):
            pdf_writer.addPage(pdf_reader.getPage(page))
        path = os.path.join(x1, filez+"_part2.pdf")
        with open(path, 'wb') as file:
            pdf_writer.write(file)
    else:
        try:
            assert x < pdf_reader.numPages
            pdf_writer1 = PdfFileWriter()
            pdf_writer2 = PdfFileWriter()

            for page in range(x+1):
                pdf_writer1.addPage(pdf_reader.getPage(page))

            for page in range(x+1, pdf_reader.getNumPages()):
                pdf_writer2.addPage(pdf_reader.getPage(page))
            path = os.path.join(x1, filez+"_part1.pdf")
            with open(path, 'wb') as file1:
                pdf_writer1.write(file1)
            path = os.path.join(x1, filez+"_part2.pdf")
            with open(path, 'wb') as file2:
                pdf_writer2.write(file2)

        except AssertionError as e:
            print("Error: The PDF you are cutting has less pages than you want to cut!")
