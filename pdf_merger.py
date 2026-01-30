from pypdf import PdfWriter
import os

#input and output folder location
path_input = "C:/Users/Laurenz Clyde/Desktop/pdf_merger/input_files"
path_output = "C:/Users/Laurenz Clyde/Desktop/pdf_merger/output_files"

#merger
pdfs = os.listdir(path_input)
#sort the files alphabetically or numerically for pages
pdfs.sort()

merger = PdfWriter()


for pdf in pdfs:
  merger.append(path_input + '\\' + pdf)

output_name = input("Output name of pdf: ")
merger.write(path_output+ '\\' + output_name + ".pdf")

#remove the input files after combining
for pdf in pdfs:
  os.remove(path_input + '\\' + pdf) 


merger.close()
