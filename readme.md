This repository contains my prominent works in the field of Artificial Intelligence, Machine Learning, Data Science, and Python programming.

Each project is structured as follows (except LogicGatesDataframes and DataViz):-

1. There is a file named in the format **project_name.py**, which contains a class of all the methods used in the project.

2. In the **main.py**, the code to execute the project and obtain the output is written.

The description of each project is shown below:-

i) _DataViz_: Sample data visualization tasks using Tableau and Microsoft Excel. The dataset using the Tableau workbook was extracted using the following Python code:-

```
import seaborn as sns
import pandas as pd
tips = sns.load_dataset("tips")
tips.to_csv("tips_dataset.csv", index=None)
```

ii) _doctrOCR_: Detects, extracts and stores text obtained from image-based PDFs/files using the in-built docTR OCR module. To use this module for your use-case, make sure that the following modules are installed:-

```
!pip install python-doctr
!pip install "python-doctr[tf]"
!pip install "python-doctr[torch]"
!pip install pillow
```

iii) _EncryptedPDFManagement_: Deals with encrypted PDF files. Make sure that the **fitz** module is available through the following installation:-

```
!pip install PyMuPDF
```

iv) _LogicGatesDataframes_: Contains code(s) to implement the 7 basic logic gates, and a working example to show how they can be used to perform efficient dataframe operations.

v) _PDFClassifier_: Identifies if a given PDF file is text-based (digital) or image-based (scanned). Again, the **fitz** module is necessary to execute this project:-

```
!pip install PyMuPDF
```

vi) _SensorNoiseFilters_: Builds a user interface (UI) to visualize noise filters for data obtained from real-time sensor readings.

vii) _XMLDataManagement_: Converts simple XML files to Pandas data frames, and complex ones to JSON. Note that, since the method of extracting records from the XML file depends on its tree structure, a standard method is not available. However, you can tweak the existing ones according to your use-case(s) and include them as methods in the class. 

The methods and classes in each project are documented using the [Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html), and the codes follow [PEP8 style guidelines](https://peps.python.org/pep-0008/).

Also, feel free to check out my technical content and profile through the following links:- 

Medium: https://medium.com/@bhargav.sridhar

LinkedIn: https://www.linkedin.com/in/bhargav-sridhar-352288188/