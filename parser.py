import PyPDF2
import os

input_pat = input("Choose patterns to look for: ")
patterns = input_pat.split()         #allows you look for several patterns at the same time
dir = '/home/xenakrll/Documents/articles/for_overview'
for filename in os.listdir(dir):
    pdfFileObj = open(os.path.join(dir)+'/'+filename, 'rb')
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        text = ''
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = text + pageObj.extractText()        #collects texts from each page into one string
        if text.find('a') == -1:
            print(filename+': search does not work')   #checks if search works in this file
        else:
            for pattern in patterns:
                if text.find(pattern) != -1:
                    print(filename+':  '+'Pattern '+pattern+'  found')
    except Exception:
        print(filename+': file is unreadable')
