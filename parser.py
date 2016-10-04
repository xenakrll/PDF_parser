import PyPDF2
import os

dir = '/home/xenakrll/Documents/articles/for_overview/2000-2005'
for filename in os.listdir(dir):
    pdfFileObj = open(os.path.join(dir)+'/'+filename, 'rb')
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        text = ''
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = text + pageObj.extractText()
        pattern = 'reentry'
        if text.find(pattern) == -1:
            print(filename+':  '+'Pattern not found')
        else:
            print(filename+':  '+'Found')
    except Exception:
        print(filename+': file is unreadable')

#print(text)