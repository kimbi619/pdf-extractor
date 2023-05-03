import PyPDF2
import requests
import json


class GCE_Extraction(object):
    def __init__(self, filename=None):
        self.filename = filename

    def get(self):
        file = open('20.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(file)
        print('number of pages = ', format(pdfReader.numPages))
        # self.get_all_pages(pdfReader)
        print(pdfReader.getPage(0).extractText())

    def get_all_pages(self, pdf):
        while pdf.getPage():
            print(pdf.extractText())


GCE_Extraction('test.pdf').get()
