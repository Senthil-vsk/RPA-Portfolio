import pdfplumber
import pandas as pd

def extract_pdf_to_excel(pdf_path, excel_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        all_data = []
        for page in pages:
            table = page.extract_table()
            for row in table:
                all_data.append(row)
        df = pd.DataFrame(all_data[1:], columns=all_data[0])
        df.to_excel(excel_path, index=False)
        
# Usage example
extract_pdf_to_excel('sample_invoice.pdf', 'output.xlsx')
