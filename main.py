import streamlit as st
from Utils.functionHelper import c_to_d, copypdf, delete_pg, extract_txt, extractImage, extractTables, merge, splitPdf

st.title('Howdy!')

# creating UI menu
menu = ["PDF", "Coming Soon..."]
choice = st.sidebar.selectbox("select for processing...", menu)

# starting code for image
if choice == 'PDF':
    st.subheader("PDF OPERATIONS")
    operations = st.radio(
        'Select Type of Operation',
        ('Merge Pdfs',"Split PDF", 'Delete pages', 'Convert to Docx', 'Extract All Images', 'Extract Text', 'Extract Tables', 'Make a copy'))
    if operations == "Merge Pdfs":
        merge()
    if operations == "Delete pages":
        delete_pg()
    if operations == "Convert to Docx":
        c_to_d()
    if operations == "Extract Text":
        extract_txt()
    if operations == "Make a copy":
        copypdf()
    if operations == "Extract All Images":
        extractImage()
    if operations == "Extract Tables":
        extractTables()
    if operations == "Split PDF":
        splitPdf()
