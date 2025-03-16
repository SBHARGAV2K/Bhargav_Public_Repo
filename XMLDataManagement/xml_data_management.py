from lxml import etree
from collections import Counter
import pandas as pd
import json

class XMLDataManagement:
    """
    Class to manage XML data

    :param file_path: path to the XML file
    :type file_path: `str`
    """

    def __init__(self, file_path):
        """Constructor method
        """
        self.xml_path = file_path

        with open(self.xml_path,'r') as f:
            self.root = etree.fromstring(f.read())

    def view_xml_tree_structure(self):
        """
        Method to view the XML tree structure
        """
        try:
            tree = etree.ElementTree(self.root)

            for tag in self.root.iter():
                path = tree.getpath(tag)
                path = path.replace('/', '    ')
                spaces = Counter(path)
                tag_name = path.split()[-1].split('[')[0]
                tag_name = ' ' * (spaces[' '] - 4) + tag_name
                print(tag_name)
        
        except Exception as ex:
            print(
                f"Exception while viewing XML tree structure: {ex}"
            )

    def save_as_csv(self, records, file_name):
        """
        Method to save records as CSV

        :param records: XML records extracted
        :type records: `dict`
        
        :param file_name: name of CSV file to save
        :type file_name: `str`
        """
        try:
            df = pd.DataFrame(records)
            df.to_csv(file_name, index=False)

        except Exception as ex:
            print(
                f"Exception while writing XML to CSV: {ex}"
            )
    
    def save_as_json(self, records, file_name):
        """
        Method to save records as JSON

        :param records: XML records extracted
        :type records: `dict`
        
        :param file_name: name of JSON file to save
        :type file_name: `str`
        """
        try:
            with open(file_name, "w") as f:
                f.write(json.dumps(records, indent=2))
            f.close()

        except Exception as ex:
            print(
                f"Exception while writing XML to JSON: {ex}"
            )