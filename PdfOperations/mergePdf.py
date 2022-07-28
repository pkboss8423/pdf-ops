from PyPDF2 import PdfFileMerger
import os

from Utils.createFolder import  create_pdf_folder

def pdf_merger(st,pdf_files):
    merger = PdfFileMerger(strict=False)
    #Iterate over the list of file names
    for pdf_file in pdf_files:
        #Append PDF files
        merger.append(pdf_file)
    x = create_pdf_folder()
    path = os.path.join(x, "merged_file.pdf")
    #Write out the merged PDF
    merger.write(path)
    merger.close()
    
    st.write(f"Process Completed. File Saved at {path}")
