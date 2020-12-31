import PyPDF2 


file = open('test.pdf', 'rb')

reader = PyPDF2.PdfFileReader(file)

n = reader.numPages

for i in range (n):
    print(i)













