import PyPDF2

pdfFileObj = open('/home/xenakrll/Documents/articles/for_overview/19/996_Detection_Algorithms_in_Implantable_Cardioverter_Defibrillators.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
text = ''
for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = text + pageObj.extractText()
pattern = 'elephant'
if text.find(pattern) == -1:
    print('Failure')
else:
    print('Found')
#print(text)