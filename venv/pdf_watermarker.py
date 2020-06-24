import sys,os
import PyPDF2


'''

How to us the script : python pdf_watermarker.py  input_folder/ output_folder/

Example: python pdf_watermarker.py  files/ marked/

'''
try:
    input_folder = sys.argv[1] #getting the folder where the pdf files are located
    output_folder = sys.argv[2] #getting the output folder

    if not os.path.isdir(output_folder) : #checking if the destination folder doesn't exist, then create it
        os.makedirs(output_folder)

    watermark = PyPDF2.PdfFileReader(open(f'{input_folder}watermarker.pdf','rb'))

    print('maring pdf files....')

    for pdf in os.listdir(input_folder) : #loop trough the pdf files and open them(read)
        current_pdf = PyPDF2.PdfFileReader(open(f'{input_folder}{pdf}','rb'))
        current_pdf_clean_name = os.path.splitext(pdf)[0]
        final_pdf = PyPDF2.PdfFileWriter()
        for i in range(current_pdf.getNumPages()) : #loop trough the pages in each pdf file and merge them with the marker
            page = current_pdf.getPage(i)
            page.mergePage(watermark.getPage(0))
            final_pdf.addPage(page)

        if not os.path.isfile(f'{output_folder}{current_pdf_clean_name}.pdf') :
            with open (f'{output_folder}{current_pdf_clean_name}.pdf', 'wb') as file:
                final_pdf.write(file)
        else:
            print(f'{current_pdf_clean_name}.pdf already exist in {output_folder}')

except (IndexError,FileNotFoundError) as error: #handling errors
    print(f"looks like something isn't not right,\n you might want to have a look on this : {error}")
else:
    print('Pdf files marked successfully')