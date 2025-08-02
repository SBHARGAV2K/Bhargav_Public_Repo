from xml_data_management import XMLDataManagement
from datetime import datetime

if __name__ == '__main__':
    # xml_path = 'books.xml'
    xml_path = 'purchase_orders.xml'
    
    xml_obj = XMLDataManagement(xml_path)

    # xml_obj.view_xml_tree_structure()

    if xml_path == 'books.xml':
        csv_output_path = 'books_list.csv'
        
        books_list = []
        for child in xml_obj.root:
            print(child.attrib)
            obj = {}
            for subchild in child:
                child.attrib[subchild.tag] = subchild.text
                if subchild.tag == 'author':
                    child.attrib[subchild.tag] = ' '.join(subchild.text.split(', ')\
                                                    [::-1])
                elif subchild.tag == 'description':
                    child.attrib[subchild.tag] = subchild.text.replace("\n", "")
                    
                elif subchild.tag == 'price':
                    child.attrib[subchild.tag] = subchild.text
                
                elif subchild.tag == 'publish_date':
                    child.attrib[subchild.tag] = datetime.strptime(
                                                    subchild.text,
                                                    '%Y-%m-%d'
                                                ).strftime('%d-%m-%Y')
            books_list.append(dict(child.attrib))
        
        xml_obj.save_as_csv(books_list, csv_output_path)
        print(
            f"Succesfully saved the XML records as CSV in {csv_output_path}"
        )


    elif xml_path == 'purchase_orders.xml':
        json_output_path = 'purchase_data.json'
        
        purchases = []
        for child in xml_obj.root:
            data = {}    
            for att in child.attrib.keys():
                if att == 'OrderDate':
                    data[att] = datetime.strptime(
                        child.attrib[att],
                        '%Y-%m-%d'
                    ).strftime('%d-%m-%Y')
                else:
                    data[att] = child.attrib[att]
            data["Address"] = []
            data["Items"] = []
            for subchild in child:
                if subchild.tag == 'Address':
                    address = {}
                    for att2 in subchild.attrib.keys():
                        address[att] = subchild.attrib[att2]
                    for add_ele in subchild:
                        if add_ele.tag == 'Zip':
                            address[add_ele.tag] = int(add_ele.text)
                        else:
                            address[add_ele.tag] = add_ele.text
                    data[subchild.tag].append(address)
                elif subchild.tag == 'Items':
                    for item in subchild:
                        items = {}
                        for att3 in item.attrib.keys():
                            items[att3] = item.attrib[att3]
                        print(items)
                        for i in item:
                            items[i.tag] = i.text
                            if i.tag == 'Quantity':
                                items[i.tag] = int(i.text)
                            elif 'Price' in i.tag:
                                items[i.tag] = float(i.text)
                            elif i.tag == 'ShipDate':
                                items[i.tag] = datetime.strptime(
                                                    i.text,
                                                    '%Y-%m-%d'
                                                ).strftime('%d-%m-%Y')
                            data[subchild.tag].append(items)
                else:
                    data[subchild.tag] = subchild.text
            purchases.append(data)

        xml_obj.save_as_json(purchases, json_output_path)
        print(
            f"Succesfully saved the XML records as JSON in {json_output_path}"
        )