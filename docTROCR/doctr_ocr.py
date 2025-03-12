from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import math

class DocTROCR:
    """
    Class to extract text from a document using docTR OCR model.

    :param model: docTR OCR model
    :type model: `doctr.models.ocr_predictor`
    """
    
    def __init__(self):
    """Constructor method
    """
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

    def get_coordinates(self, output):
    """
    
    """
        page_dim = output['pages'][0]["dimensions"]
        text_coordinates = []
        for obj1 in output['pages'][0]["blocks"]:
            for obj2 in obj1["lines"]:
                for obj3 in obj2["words"]:                
                    converted_coordinates = convert_coordinates(
                                               obj3["geometry"],page_dim
                                              )
                    print("{}: {}".format(converted_coordinates,
                                          obj3["value"]
                                          )
                         )
                    text_coordinates.append(converted_coordinates)
        return text_coordinates

