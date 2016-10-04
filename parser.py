import PyPDF2
import os

input_pat = input("Choose pattern to look for: ")
patterns = input_pat.split()
dir = '/home/xenakrll/Documents/articles/for_overview/2000-2005'
for filename in os.listdir(dir):
    pdfFileObj = open(os.path.join(dir)+'/'+filename, 'rb')
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        text = ''
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = text + pageObj.extractText()
        for pattern in patterns:
            if text.find(pattern) == -1:
                print(filename+':  '+'Pattern '+pattern+' not found')
            else:
                print(filename+':  '+pattern+' found')
    except Exception:
        print(filename+': file is unreadable')

#print(text)