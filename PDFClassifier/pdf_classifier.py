import fitz

class PDFClassifier:
    """
    Class to classify PDF as text-based or image-based.

    :param pdf_file: path to the PDF file
    :type pdf_file: `str`
    """
    def __init__(self, pdf_file):
        """
        Constructor method
        """
        self.pdf_file = pdf_file

    def classify_pdf(self):
        """
        Function to classify PDF as text-based or image-based.

        :param pdf_file: path to the PDF file
        :type pdf_file: `str`

        :raises Exception: If an error occurs while classifying PDF

        :return: list of classification results
        :rtype: `list`
        """
        try:
            with open(self.pdf_file,"rb") as f:
                pdf = fitz.open(f)
                res = []
                for page in pdf:
                    image_area = 0.0
                    text_area = 0.0
                    for b in page.get_text("blocks"):
                        if '<image:' in b[4]:
                            r = fitz.Rect(b[:4])
                            image_area = image_area + abs(r)
                        else:
                            r = fitz.Rect(b[:4])
                            text_area = text_area + abs(r)
                    if image_area == 0.0 and text_area != 0.0:
                        res.append(1)
                    if text_area == 0.0 and image_area != 0.0:
                        res.append(0) 
                return res
        except Exception as ex:
            raise Exception(
                f"Error in classifying PDF: {ex}"
            )