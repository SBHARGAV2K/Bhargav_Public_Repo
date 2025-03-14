from encrypted_pdf_management import EncryptedPDFManagement
from getpass import getpass

if __name__ == '__main__':
    pdf_file_path = "password_pdf.pdf" #Specify your PDF path here
    pdf_obj = EncryptedPDFManagement(pdf_file_path)

    if pdf_obj.is_password_protected_pdf():
        password = getpass("Enter password to decrypt PDF:")
        pdf_obj.decrypt_pdf(pdf_file_path, password)
    else:
        print("PDF is not password protected!")