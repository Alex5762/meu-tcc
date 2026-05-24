import pandas as pd
import docx

def read_excel(file_path):
    print(f'--- EXCEL: {file_path} ---')
    df = pd.read_excel(file_path)
    print(df.to_string())

def read_docx(file_path):
    print(f'--- DOCX: {file_path} ---')
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        print(para.text)

read_excel(r'C:\Users\josep\Downloads\NOTAS_TRABALHO_PYTHON_-_NF_-_Modelo.xlsx')
read_docx(r'C:\Users\josep\Downloads\ROTEIRO_DE_EXTENS_O.docx')
