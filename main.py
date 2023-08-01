import PyPDF2

pdfiles = ["1.pdf", "2.pdf", "sample.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()

with open('merged.pdf', 'wb') as mergedFile:
    merger.write(mergedFile)
