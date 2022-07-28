import os
def create_pdf_folder():
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, 'Downloads')
    if not os.path.exists(path+"/Pdf_here"):
        os.makedirs(path+"/Pdf_here")
    path = os.path.join(userprofile, 'Downloads', 'Pdf_here')
    return path

def create_images_folder():
    path=create_pdf_folder()
    if not os.path.exists(path+"/Pdf_images"):
        os.makedirs(path+"/Pdf_images")
    path = os.path.join(path, 'Pdf_images')
    return path

def create_tables_folder():
    path=create_pdf_folder()
    if not os.path.exists(path+"/Pdf_tables"):
        os.makedirs(path+"/Pdf_tables")
    path = os.path.join(path, 'Pdf_tables')
    return path

def create_splitpdf_folder():
    path=create_pdf_folder()
    if not os.path.exists(path+"/Split_pdfs"):
        os.makedirs(path+"/Split_pdfs")
    path = os.path.join(path, 'Split_pdfs')
    return path



