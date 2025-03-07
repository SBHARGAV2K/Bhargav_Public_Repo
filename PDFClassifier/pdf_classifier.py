import fitz

def classifier(pdf_file):
    with open(pdf_file,"rb") as f:
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
    
if __name__ == '__main__':
    file_path = '' #Specify PDF path here
    classifier_result = classifier(file_path)
    if 0 in classifier_result:
        print("PDF is image-based!")
    else:
        print("PDF is text-based!")