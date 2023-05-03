import pdfplumber

with pdfplumber.open('test.pdf') as pdf:
    for page in pdf.pages:
        text1 = page.extract_text()
        print(text1)
    txt_file = open("test5.txt",mode='a',encoding='utf-8')
    txt_file.write(text1)