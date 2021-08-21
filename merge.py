import sys
from PyPDF2 import PdfFileMerger, PdfFileReader

filename1 = input("First PDF filename: ") #'./UW-Immunity-Verification-Form.pdf'
filename2 = input("Second PDF filename: ") #'./Visit_Summary_With_Immunization.pdf'
output = input("Output filename: ") #'./Matt_Guo_Immunization.pdf'
merger = PdfFileMerger()

merger.append(PdfFileReader(open(filename1, 'rb')))
merger.append(PdfFileReader(open(filename2, 'rb')))

merger.write(output)
