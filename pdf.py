# install PyPDF2
import PyPDF2

with open('dummy.pdf', 'rb') as file: # rb stands for read and binary
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90) # Rotate the page, this only works on page
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)