from doctr_ocr import DocTROCR

if __name__ == '__main__':
    file_path = '' #Specify PDF path here
    doctr_ocr = DocTROCR(file_path)
    ocr_output = doctr_ocr.get_ocr_output()
    doctr_ocr.write_ocr_output(ocr_output)