
'''this script will add pages 1,3,4 from all PDFs into a file'''

from PyPDF2 import PdfFileWriter, PdfFileReader
from os import getcwd,listdir

# get all the relevant files names as a list
path = os.getcwd()
file_list = os.listdir(path)

names = []
for item in file_list:
    if item[0:9] == 'Statement':
        names.append(item)
print(names)

# open the files to get a fileobject
file_objects = []
for objects in names:
    x = PdfFileReader(open(objects,"rb"))
    file_objects.append(x)
    
# mention which Page Numbers to add:
page_numbers = [0,2,3]

# instantiate a PdfFileWriter object
file_to_write = PdfFileWriter()

# add the three pages from each of the pdf file
for pdf in file_objects:
    for number in page_numbers:
        print("adding PDF {} page number {}".format(pdf,number))
        file_to_write.addPage(pdf.getPage(number))

# make a PDF
output_pdf = open("output.pdf", "wb")
file_to_write.write(output_pdf)

# close the files we opened
output_pdf.close()
