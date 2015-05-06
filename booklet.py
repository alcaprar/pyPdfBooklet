from pyPdf import PdfFileWriter, PdfFileReader
output_pdf = PdfFileWriter()

with open(r'input.pdf', 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)
    total_pages = input_pdf.getNumPages()
    print "pagine totali "+str(total_pages)

    numPagine= total_pages

    while not (numPagine % 4 ==0):
        numPagine+=1
    primaMeta= range(1,numPagine/2+1,1)
    secondaMeta= range(numPagine,numPagine/2,-1)


    sequenza = []

    for x in range(0,numPagine/2,1):
        if(x%2==0):
            sequenza.append(secondaMeta[x])
            sequenza.append(primaMeta[x])
        else:
            sequenza.append(primaMeta[x])
            sequenza.append(secondaMeta[x])

    for item in sequenza:
        print item
        if(item>total_pages):
            output_pdf.addBlankPage
        else:
            output_pdf.addPage(input_pdf.getPage(item-1))
    with open(r'output.pdf', "wb") as writefile:
        output_pdf.write(writefile)    
