import fitz
from getpass import getpass

#Method 1
def is_password_protected_pdf(pdf_file_path):
    doc = fitz.Document(pdf_file_path)
    if doc.needs_pass:
        return True
    return False

# #Method 2
# def is_password_protected_pdf(pdf_file_path):
#     doc = fitz.Document(pdf_file_path)
#     if doc.metadata is None:
#         return True
#     return False

def is_pdf_text_encrypted(pdf_file_path):
    doc = fitz.Document(pdf_file_path)
    if doc.metadata["encryption"] is not None:
        return True
    return False

def decrypt_pdf(pdf_file_path, password):
    doc = fitz.Document(pdf_file_path)
    if doc.authenticate(password):
        file_name = "pdf_decrypted.pdf"
        doc.save(file_name)
        print("\Successfully decrypted PDF")
    else:
        print("\t Password incorrect!! Cannot decrypt PDF!!!")


if __name__ == '__main__':
    pdf_file_path = "password_pdf.pdf" #Specify your PDF path here
    if is_password_protected_pdf(pdf_file_path):
        password = getpass("Enter password to decrypt PDF:")
        decrypt_pdf(pdf_file_path, password)
    else:
        print("PDF is not password protected!")