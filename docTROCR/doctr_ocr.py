from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import math

class DocTROCR:
    """

    """
    
    def __init__(self):
    """Constructor method
    """

    def convert_coordinates(self, geometry, page_dim):
    """

    """    
        len_x = page_dim[1]
        len_y = page_dim[0]
        (x_min, y_min) = geometry[0]
        (x_max, y_max) = geometry[1]
        x_min = math.floor(x_min * len_x)
        x_max = math.ceil(x_max * len_x)
        y_min = math.floor(y_min * len_y)
        y_max = math.ceil(y_max * len_y)
        return [x_min, x_max, y_min, y_max]

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

