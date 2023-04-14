import PyPDF2

solo = input('Digite qual solo você deseja? ').title()

with open('/home/erickom/Downloads/Doc-169-Perguntas-e-Respostas.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    number_of_pages = len(pdf_reader.pages)
    for page_number in range(number_of_pages):
        page = pdf_reader.pages[page_number]
        page_content = page.extract_text()
        if 'Quais as principais características dos {}'.format(solo) in page_content:
            print(page_content)
   