import sys,os
import PyPDF2

'''

How to us the script : python pdf_merger.py  input_folder/

Example: python pdf_merger.py  files/



'''

try:
    input_folder = sys.argv[1] #getting the folder where the pdf files are located
    pdf_merged = PyPDF2.PdfFileMerger()
    for pdf in os.listdir(input_folder) :
        pdf_merged.append(f'{input_folder}{pdf}') #merging the pdf files

    if not os.path.isfile(f'{input_folder}merged.pdf') : #checking if merged.pdf doesn't already exist
        pdf_merged.write(f'{input_folder}merged.pdf') #saving the merged pdf
    else:
        pdf_merged.write(f'{input_folder}merged2.pdf')  # saving the merged pdf

except (IndexError,FileNotFoundError) as error: #handling errors
    print(f"looks like something isn't not right,\n you might want to have a look on this : {error}")
else:
    print('Pdf merge success ')