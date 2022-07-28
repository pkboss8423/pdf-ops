import fitz
import io
from PIL import Image
import os
from Utils.createFolder import create_images_folder, create_pdf_folder
from pdf2docx import Converter
# file path you want to extract images from

def extract_images(st,file):
    # open the file
    filename = os.path.basename(file)
    filename = filename.split(".")
    filename = filename[0] 
    pdf_file = fitz.open(file)
    x = create_images_folder()
    # iterate over PDF pages
    c = 0
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        if image_list:
            st.write(
                f"[+] Found a total of {len(image_list)} images in page {page_index}")
            c += len(image_list)
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            path = os.path.join(
                x, f"image{page_index+1}_{image_index}.{image_ext}")
            image.save(open(path, "wb"))
    print("Total images in document:", c)


    def create_blank_pdf():
        from PyPDF2 import PdfFileWriter
        pdf_writer = PdfFileWriter()
        from pathlib import Path

        
        x = create_pdf_folder()
        path = os.path.join(x, filename+"_Images.pdf")
        with Path(path).open(mode="wb") as output_file:
            pdf_writer.write(output_file)
        return path


    x = create_blank_pdf()
    doc = fitz.open(x)
    imgdir = create_images_folder()  # where the pics are
    imglist = os.listdir(imgdir)  # list of them
  # pic count
    for i, f in enumerate(imglist):
        img = fitz.open(os.path.join(imgdir, f))  # open pic as document
        rect = img[0].rect  # pic dimension
        pdfbytes = img.convert_to_pdf()  # make a PDF stream
        img.close()  # no longer needed
        imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
        page = doc.new_page(width=rect.width,
                            height=rect.height)
        page.show_pdf_page(rect, imgPDF, 0)

    x = create_pdf_folder()
    path1 = os.path.join(x, filename+"_Images.pdf")
    doc.saveIncr()
    doc.close()
    x = create_pdf_folder()
    path = os.path.join(x, filename+"_Images.docx")
    cv = Converter(path1)
    cv.convert(path, start=0, end=None)
    cv.close()
    st.write(f"Process Completed. File Saved at {path}")
