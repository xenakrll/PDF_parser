import PyPDF2
import os

input_pat = 'sorting chip throughput' #input("Choose patterns to look for: ")
patterns = input_pat.split()         #allows you look for several patterns at the same time split by space
dir = '/home/xenakrll/Documents/EMBL_Merten/papers'
for filename in os.listdir(dir):
    pdfFileObj = open(os.path.join(dir)+'/'+filename, 'rb') #will not work if the file name is with spaces
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        text = ''
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = text + pageObj.extractText()        #collects texts from each page into one string
        #if text.find('a') == -1:
            #print(filename+': search does not work')   #checks if search works in this file
        for pattern in patterns:
            if text.find(pattern) != -1:
                print(filename+':  '+'Pattern '+pattern+'  found')
    except Exception:
        print(' ')
        print(filename+': file is unreadable') #if the formatting is not suitable or something else happens
