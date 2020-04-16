import PyPDF2
import os.path
from modules.mytools import MyTools

class MergePDF:
    merge_name = ""

    def pdf_combine(self,pdf_list,save_to):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        if len(self.merge_name)  == 0:
            self.merge_name = 'merge.pdf'
        elif '.pdf' not in self.merge_name:
            self.merge_name += '.pdf'
        merger.write(save_to + "//" + self.merge_name)
        print(f'\nMerged PDF saved to:{save_to}')

    def start(self):
        print('*** Merge PDFs ***')
        count_pdf = 0
        save_to = ''
        pdf = ''
        pdf_inputs = []
        while pdf != '1':
            pdf = input('Insert path to PDF. When done, enter [1]\n')
            if '.pdf' not in pdf and pdf != '1':
                pdf += '.pdf'
            if pdf != '1':
                if os.path.isfile(pdf):
                    f = open(pdf)
                    save_to = os.path.dirname(f.name) # Get last path name
                    pdf_inputs.append(pdf)
                    count_pdf += 1
                    print(f'\n{count_pdf} PDFs added. \n')
                else:
                    print('PDF file is not exist! Insert full path including PDF name!')

        if count_pdf == 0:
            print('PDFs not found.')
        else:
            self.merge_name = input('Enter name for your new merge PDF (leave it empty for default name merge.pdf)')
            self.pdf_combine(pdf_inputs,save_to)

        input('\nPress any key to continue . . .')
        print('###########\n\n')