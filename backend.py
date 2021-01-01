import PyPDF2
import fitz
from PIL import Image
import os


def process(fileName, uploadPath, imagePath, threshold):

    dirname = os.path.dirname(__file__)
 
    file = open(os.path.join(dirname, uploadPath + fileName), 'rb')

    reader = PyPDF2.PdfFileReader(file)

    n = reader.numPages


    doc = fitz.open(uploadPath + fileName)

    pagesToKeep = list(range(n))
     
    for i in range (n):
        deletePage = True
       
        
        
        page = doc.loadPage(i)
        pix = page.getPixmap()
        output = imagePath + "img%d.png" % (i) 
        pix.writePNG(output)


        img = Image.open(imagePath + "img%d.png" % (i)) 
        size = img.size


        width, height = size
        totalPixels = width * height

        sr,sg,sb = img.getpixel((1,1))


        maxPixels = threshold * totalPixels

        pixelCounter = 0
        
        for x in range (width):
            for y in range (height):
                r,g,b = img.getpixel((x,y))
                if (r!=sr or g!=sg or b!=sb):
                    pixelCounter +=1
                    if pixelCounter > maxPixels:
                        deletePage = False
                    
               

        if deletePage:
            pagesToKeep.remove(i)


        os.remove(imagePath + "img%d.png" % (i))     
                        

    writer1 = PyPDF2.PdfFileWriter()
    
    for i in pagesToKeep:
        x = reader.getPage(i)
        writer1.addPage(i)

    with open ('fixed_PDF', 'wb') as f:
        reader.write(f)
    


    
process('test.pdf', 'uploads\\', 'images\\', 0.1)
    
    

    















