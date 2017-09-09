from PyPDF2 import PdfFileWriter, PdfFileReader
from wand.image import Image
import image_slicer
from fpdf import FPDF
import os
filename = raw_input("Enter file name:")
inputpdf = PdfFileReader(open(filename, "rb"))
numPages = inputpdf.numPages
pagesPerSlide = 4
for i in xrange(numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("trial-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

for i in xrange(numPages):
	with Image(filename="trial-page%s.pdf" % i) as img:
	    with img.convert('png') as converted:
	        converted.save(filename="trial-page%s.png" % i)

for i in xrange(numPages):
	image_slicer.slice("trial-page%s.png" % i, 4)

imlist = []

for i in xrange(numPages):
	imlist.append("trial-page%s_01_01.png" % i)
	imlist.append("trial-page%s_01_02.png" % i)
	imlist.append("trial-page%s_02_01.png" % i)
	imlist.append("trial-page%s_02_02.png" % i)

pdf = FPDF(format='A4')
pdf.add_page()
for image in imlist:
    pdf.image(image)

pdf.output("Final.pdf", "F")

for i in xrange(numPages):
	os.remove("trial-page%s.pdf" % i)
	os.remove("trial-page%s.png" % i)
	os.remove("trial-page%s_01_01.png" % i)
	os.remove("trial-page%s_01_02.png" % i)
	os.remove("trial-page%s_02_01.png" % i)
	os.remove("trial-page%s_02_02.png" % i)
