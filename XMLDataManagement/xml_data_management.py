from lxml import etree
from collections import Counter
import pandas as pd

def view_xml_tree_structure(file_path):
    with open(file_path,'r') as f:
        root = etree.fromstring(f.read())

    tree = etree.ElementTree(root)

    for tag in root.iter():
        path = tree.getpath(tag)
        path = path.replace('/', '    ')
        spaces = Counter(path)
        tag_name = path.split()[-1].split('[')[0]
        tag_name = ' ' * (spaces[' '] - 4) + tag_name
        print(tag_name)

