import os
import PyPDF2
import streamlit as st
from PdfOperations.deletePages import create_array
from Utils.createFolder import  create_pdf_folder

def extract_text(path1,pages):
    pages=[i for i in pages.split(",")]
    z=create_array(pages)
    z.sort()
    x=create_pdf_folder()
    path=os.path.join(x,"extracted_text.txt")
    if os.path.exists(path):
        os.remove(path)
        path = os.path.join(x, "extracted_text.txt")
    file1=open(path,"a")
    with open(path1, mode='rb') as f:

        reader = PyPDF2.PdfFileReader(f, strict=False)
        for i in z:
            page = reader.getPage(i)

            x=page.extractText()
            file1.writelines(x)
    st.write(f"Process Completed. File Saved at {path}")
