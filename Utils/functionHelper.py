import os
import streamlit as st
from PdfOperations.copyPdf import copy_pdf
from PdfOperations.coverttoDocx import convert_to_docx
from PdfOperations.deletePages import delete_page
from PdfOperations.extractImages import extract_images
from PdfOperations.extractTables import extract_tables
from PdfOperations.extractText import extract_text
from PdfOperations.mergePdf import pdf_merger
from PdfOperations.splipdf import split_pdf


def save_uploaded_file(uploadedfile):
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, "Documents", uploadedfile.name)
    try:
        with open(os.path.join(userprofile, "Documents", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())
        return path
    except:
        print("Some Error")
        return ""
    
def merge():
    pdf_files = st.file_uploader(
        "Upload PDF (Select Pdf in order you want to merge)", type=['pdf'], accept_multiple_files=True)
    arr = []
    if pdf_files is not None:
        for pdf_file in pdf_files:
            # file_details = {"Filename": pdf_file.name,
                            # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

            path = save_uploaded_file(pdf_file)
            arr.append(path)
            # st.write(file_details)

    if st.button("Start"):
        pdf_merger(st, arr)


def delete_pg():
    pdf_file = st.file_uploader(
        "Upload PDF ", type=['pdf'])
    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
                        # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}
        path = save_uploaded_file(pdf_file)
        # st.write(file_details)
    inp = st.text_input("Enter pages to delete:(E.g. \"1,2,5-7\")")
    if st.button("Start"):
        delete_page(st, path, inp)


def c_to_d():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])

    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
                        # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)

        # st.write(file_details)

    if st.button("Start"):
        convert_to_docx(st, path)


def extract_txt():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])
    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
                        # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)

        # st.write(file_details)
    inp = st.text_input(
        "Enter pages to extract text from:(E.g. \"1,2,5-7\")")
    if st.button("Start"):
        extract_text(path, inp)


def copypdf():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])

    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
                        # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)

        # st.write(file_details)

    if st.button("Start"):
        copy_pdf(st, path)
        
def extractImage():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])

    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
                        # "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)

        # st.write(file_details)

    if st.button("Start"):
        extract_images(st, path)

def extractTables():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])

    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
        #                 "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)
        # st.write(file_details)

    st.write("Enter specific pages:(By default it runs all pages)")
    inp = st.text_input("Enter pages with tables:(E.g. \"5-7\")")
    if st.button("Start"):
        extract_tables(st, path, inp)
def splitPdf():
    pdf_file = st.file_uploader(
        "Upload PDF", type=['pdf'])

    if pdf_file is not None:

        # file_details = {"Filename": pdf_file.name,
        #                 "FileType": pdf_file.type, "FileSize": (pdf_file.size)}

        path = save_uploaded_file(pdf_file)
        # st.write(file_details)
    type=st.radio("Choose one:",("Split in two","Range"))
    if type == "Split in two":
        inp = st.text_input("Enter page from where you want to split ( Note: It splits upto the page number you enter.):")
    if type=="Range":
        inp = st.text_input("Enter page range  you want to split:(Eg: 3-8)")
    if st.button("Start"):
        split_pdf(st, path, inp)
    
