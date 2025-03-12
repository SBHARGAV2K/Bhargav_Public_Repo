from pdf_classifier import PDFClassifier

if __name__ == '__main__':
    file_path = 'text_based_pdf_EXAMPLE.pdf' #Specify PDF path here
    #file_path = 'image_based_pdf_EXAMPLE.pdf' #Specify PDF path here
    
    pdf = PDFClassifier(file_path)
    
    classifier_result = pdf.classify_pdf(file_path)
    
    if 0 in classifier_result:
        print("PDF is image-based!")
    else:
        print("PDF is text-based!")