import streamlit as st
from docx import Document
from fpdf import FPDF
##fuction to convert word to pdf
def convert_to_pdf(text, output_file):
    pdf=FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_file)
    
def read_word_file(file_path):
      doc=Document(file_path)
      content=[]
      for paragraph in doc.paragraphs:
            content.append(paragraph.text)
      return "\n".join(content)
    
      
col1, col2, col3=st.columns(3)
with col1:
    st.header(":red[Resume/CV]")



doc="My Resume.docx"   
pdf_file_path="Downloads"
doc_content=read_word_file(doc)     
st.text_area("", doc_content, height=800, disabled=True)
with col3:
        if st.button("📂 Download My Resume"):
             convert_to_pdf(doc_content, pdf_file_path)
             with open(pdf_file_path, "rb") as pdf_file:
                  st.download_button(label="📄Download as PDF",data=pdf_file,
                           file_name="Seth's_Resume .pdf",
                           mime="application/pdf")
        
        
