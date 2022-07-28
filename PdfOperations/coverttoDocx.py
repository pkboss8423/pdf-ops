import os
from Utils.createFolder import  create_pdf_folder
from pdf2docx import Converter


def convert_to_docx(st,file):
    filename = os.path.basename(file)
    filename = filename.split(".")
    filename = filename[0]
    x = create_pdf_folder()
    path = os.path.join(x, filename+".docx")
    cv = Converter(file)
    cv.convert(path, start=0, end=None)
    cv.close()
    
    st.write(f"Process Completed. File Saved at {path}")
