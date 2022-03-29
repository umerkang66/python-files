import PyPDF2
import sys


# READ A PDF FILE, ROTATE IT, THEN WRITE IT
# "rb" means read the binary, cause, pdfs are actually in binary forms
def pdf_read_and_write():
    with open('./pdfs/dummy.pdf', mode='rb') as dummy_pdf:
        # reader is the whole pdf, it can have multiple pages
        reader = PyPDF2.PdfFileReader(dummy_pdf)
        print(reader.numPages)
        # this will return the page obj
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        # "wb" means write binary
        with open('pdfs/tilt.pdf', 'wb') as new_file:
            writer = PyPDF2.PdfFileWriter()
            # first this page will be added in writer obj (in memory)
            writer.addPage(page)
            # then this file will be written through write obj
            writer.write(new_file)


# COMBINE TWO OR MORE PDF INTO ONE PDF
def pdf_combiner(pdf_list):
    # pdf_list is our input
    # this method will merge the pdfs into one pdf
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # here merger will automatically read the files
        # from the path provided, and merge them together
        # this will add every pdf, as a page
        merger.append(pdf)
    # we don't even have to open a file
    merger.write('./pdfs/super.pdf')


# This is going to grab all items in list, except the first one
if len(sys.argv) >= 1:
    inputs = sys.argv[1:]
    if len(inputs) >= 2:
        pdf_combiner(inputs)


def add_watermark():
    template = PyPDF2.PdfFileReader(open('./pdfs/super.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('./pdfs/wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        # for every page in template, merge the first page of watermark
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        with open('./pdfs/watermarked_output.pdf', 'wb') as file:
            output.write(file)


add_watermark()
