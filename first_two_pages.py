from PyPDF2 import PdfFileMerger
from os import getcwd,listdir


# get all the relevant files names as a list
path = os.getcwd()
file_list = os.listdir(path)

names = []
for item in file_list:
    if item[0:9] == 'Statement':
        names.append(item)
print(names)

# instantiate a merger object
merger = PdfFileMerger()

# open the files 
files = []
for objects in names:
    x = open(objects,"rb")
    files.append(x)

#add first pages to input
for i in files:
    merger.append(fileobj = i, pages = (0,1))

# Write to an output PDF document
output = open("two_pages.pdf", "wb")
merger.write(output)

# close the files we opened
output.close()

for item in files:
    print ("closing: ", item)
    item.close()
output.close()