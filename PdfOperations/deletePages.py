from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import os
from Utils.createFolder import  create_pdf_folder

def create_array(pages_to_delete):
    z = []
    for i in pages_to_delete:
        if "-" not in i:
            z.append(int(i)-1)
        else:
            i = i.split("-")
            for j in range(int(i[0]), int(i[1])+1):
                z.append(j-1)
    return z
def delete_page(st,file,pages):
    # page numbering starts from 0
    pages_to_delete = [i for i in pages.split(",")]
    z=create_array(pages_to_delete)

    #infile = PdfFileReader(file[0], 'rb')

    pdfObj = open(file, 'rb')

    infile = PdfFileReader(
        pdfObj,
        strict=False
    )
    output = PdfFileWriter()
    for i in range(len(infile.pages)):
        if i not in z:
            p = infile.getPage(i)
            output.add_page(p)
    x = create_pdf_folder()
    filename = os.path.basename(file)
    filename = filename.split(".")
    filename = filename[0]
    path = os.path.join(x, filename+"_new.pdf")
    with open(path, 'wb') as f:
        output.write(f)
        
    st.write(f"Process Completed. File Saved at {path}")
    
