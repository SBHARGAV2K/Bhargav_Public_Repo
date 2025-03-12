from doctr.models import ocr_predictor
from doctr.io import DocumentFile
import PIL
from PIL import ImageDraw
import math
import json

class DocTROCR:
    """
    Class to extract text from a document using docTR OCR model.

    :param file_path: path to the image file
    :type file_path: `str`
    """
    def __init__(self, file_path):
        """Constructor method
        """
        self.file_path = file_path
        self.model = ocr_predictor(det_arch = 'db_resnet50',    
            reco_arch = 'crnn_vgg16_bn', 
            pretrained = True
        ) 

    def convert_coordinates(self, geometry, page_dim):
        """
        Function to convert geometric coordinates to graphical coordinates.

        :param geometry: list of coordinates in geometric form ([(x_min, y_min), (x_max, y_max)])
        :type geometry: `list`
        :param page_dim: dimensions of the page ([dim_y, dim_x])
        :type page_dim: `list`

        :raises Exception: If an error occurs while converting coordinates

        :return: list of coordinates in graphical format ([x_min, x_max, y_min, y_max]) 
        :rtype: `list`
        """
        try:
            dim_x = page_dim[1]
            dim_y = page_dim[0]
            (x_min, y_min) = geometry[0]
            (x_max, y_max) = geometry[1]
            x_min = math.floor(x_min * dim_x)
            x_max = math.ceil(x_max * dim_x)
            y_min = math.floor(y_min * dim_y)
            y_max = math.ceil(y_max * dim_y)
            return [x_min, x_max, y_min, y_max]
        except Exception as ex:
            raise Exception(
                f"Error in converting coordinates: {ex}"
            )

    def get_graphical_coordinates(self, output):
        """
        Function to get graphical coordinates of the text.

        :param output: OCR output obtained from the model
        :type output: `dict`

        :raises Exception: If an error occurs while getting graphical coordinates

        :return: list of graphical coordinates of the text
        :rtype: `list`
        """
        try:
            page_dim = output['pages'][0]["dimensions"]
            text_coordinates = []
            for obj1 in output['pages'][0]["blocks"]:
                for obj2 in obj1["lines"]:
                    for obj3 in obj2["words"]:                
                        converted_coordinates = self.convert_coordinates(
                                                obj3["geometry"],page_dim
                                                )
                        print("{}: {}".format(converted_coordinates,
                                            obj3["value"]
                                            )
                            )
                        text_coordinates.append(converted_coordinates)
            return text_coordinates

        except Exception as ex: 
            raise Exception(
                f"Error in getting graphical coordinates: {ex}"
            )

    def get_ocr_output(self):
        """
        Function to get the output of the OCR model.

        :raises Exception: If an error occurs while getting OCR output

        :return: OCR output
        :rtype: `dict`
        """
        try:
            img = DocumentFile.from_images(self.file_path)
            result = self.model(img)
            self.output = result.export()
            return self.output
        except Exception as ex:
            raise Exception(
                f"Error in getting OCR output: {ex}"
            )
    
    def show_ocr_output(self):
        """
        Function to display the output of the OCR model.

        :raises Exception: If an error occurs while displaying OCR output
        """
        try:
            for obj1 in self.output['pages'][0]["blocks"]:
                for obj2 in obj1["lines"]:
                    for obj3 in obj2["words"]:
                        print("{}: {}".format(obj3["geometry"],obj3["value"]))
        except Exception as ex:
            raise Exception(
                f"Error in displaying OCR output: {ex}"
            )

    def write_ocr_output(self, output):
        """
        Function to write the output to a JSON file.

        :param output: OCR output obtained from the model
        :type output: `dict`

        :raises Exception: If an error occurs while writing output to a JSON file
        """
        try:
            with open("path/docTROCR_sample_output.json", "w") as f:
                f.write(json.dumps(output, indent=1))
            f.close()
        except Exception as ex:
            raise Exception(
                f"Error in writing output: {ex}"
            )
        
    def draw_bounding_boxes(self, image, bound):
        """
        Function to draw bounding boxes on the image."

        :param image: image on which bounding boxes are to be drawn
        :type image: `PIL.Image`
        :param bound: list of bounding boxes
        :type bound: `list`

        :raises Exception: If an error occurs while drawing bounding boxes

        :return: image with bounding boxes drawn
        :rtype: `PIL.Image`
        """
        try:
            draw = ImageDraw.Draw(image)
            for b in bound:
                p0, p1, p2, p3 = [b[0],b[2]], [b[1],b[2]], \
                                [b[1],b[3]], [b[0],b[3]]
                draw.line([*p0,*p1,*p2,*p3,*p0], fill='blue', width=2)
            return image
        except Exception as ex:
            raise Exception(
                f"Error in drawing bounding boxes: {ex}"
            )