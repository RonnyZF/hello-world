import xml.etree.ElementTree as ET
import pandas as pd

def xml_to_dataframe(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tables = []
    for table in root.iter('TABLE'):
        rows = []
        for row in table.iter('ROW'):
            cells = []
            for cell in row:
                text = None
                for child in cell:
                    if child.text:
                        text = child.text
                cells.append(text)
            rows.append(cells)
        tables.append(pd.DataFrame(rows[1:], columns=rows[0]))

    return tables

if __name__ == "__main__":
    tables = xml_to_dataframe('4230_file.xml')
    for i, table in enumerate(tables):
        print(f'Table {i + 1}:')
        print(table)
        print('\n---\n')
