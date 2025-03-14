import fitz

class EncryptedPDFManagement:
    """
    Class to manage encrypted PDF files    
    
    :param pdf_file_path: path to the PDF file
    :type pdf_file_path: `str`
    """

    def __init__(self, pdf_file_path):
        """Constructor method
        """
        self.pdf_file_path = pdf_file_path
    
    #Method 1
    def is_password_protected_pdf(self):
        """
        Function to check if the PDF is password protected or not.

        :raises Exception: If an error occurs while checking if the PDF is password protected

        :return: if the PDF is password protected or not
        :rtype: `bool`
        """
        try:
            doc = fitz.Document(self.pdf_file_path)
            if doc.needs_pass:
                return True
            return False
        except Exception as ex:
            raise Exception(
                f"Error in checking if the PDF is password protected: {ex}"
            )

    #Method 2
    # def is_password_protected_pdf(self):
    #     """
    #     Function to check if the PDF is password protected or not.

    #     :raises Exception: If an error occurs while checking if the PDF is password protected
    
    #     :return: if the PDF is password protected or not
    #     :rtype: `bool`
    #     """
    #     try:
    #         doc = fitz.Document(self.pdf_file_path)
    #         if doc.metadata is None:
    #             return True
    #         return False
    #     except Exception as ex:
    #         raise Exception(
    #             f"Error in checking if the PDF is password protected: {ex}"
    #         )
    
    def is_pdf_text_encrypted(self):
        """
        Function to check if the text in the PDF is encrypted or not.

        :raises Exception: If an error occurs while checking if the text in the PDF is encrypted

        :return: if the text in the PDF is encrypted or not
        :rtype: `bool`
        """
        try:
            doc = fitz.Document(self.pdf_file_path)
            if doc.metadata["encryption"] is not None:
                return True
            return False
        
        except Exception as ex:
            raise Exception(
                f"Error in checking if the text in the PDF is encrypted: {ex}"
            )

    def decrypt_pdf(self, password):
        """
        Function to decrypt the PDF file."
        
        :param password: password to decrypt the PDF
        :type password: `str`

        :raises Exception: If an error occurs while decrypting the PDF

        :return: None
        :rtype: None
        """
        try:
            doc = fitz.Document(self.pdf_file_path)
            if doc.authenticate(password):
                file_name = "pdf_decrypted.pdf"
                doc.save(file_name)
                print("\Successfully decrypted PDF")
            else:
                print("\t Password incorrect!! Cannot decrypt PDF!!!")
        
        except Exception as ex:
            raise Exception(
                f"Error in decrypting PDF: {ex}"
            )