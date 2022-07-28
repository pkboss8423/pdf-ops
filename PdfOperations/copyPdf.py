import os
from Utils.createFolder import  create_pdf_folder
from PyPDF2 import PdfFileWriter,PdfFileReader
from pathlib import Path


def copy_pdf(st,file):
    pdfwriter=PdfFileWriter()
    reader = PdfFileReader(file, strict=False)
    for i in range(reader.numPages):
        page = reader.getPage(i)
        pdfwriter.add_page(page)
    filename = os.path.basename(file)
    filename = filename.split(".")
    filename = filename[0]
    x = create_pdf_folder()
    path = os.path.join(x, filename+"_copy.pdf")
    with Path(path).open(mode="wb") as output_file:
        pdfwriter.write(output_file)
    st.write(f"Process Completed. File Saved at {path}")
