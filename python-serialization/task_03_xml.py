#!/usr/bin/python3
"""Module for XML serialization and deserialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to a file.

    Args:
        dictionary (dict): Dictionary with string keys and values to serialize
        filename (str): Output filename for the XML file
    """
    # Create root element
    root = ET.Element("data")

    # Add child elements for each key-value pair
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create XML tree
    tree = ET.ElementTree(root)

    # Add indentation for readability (Python 3.9+)
    if hasattr(ET, 'indent'):
        ET.indent(tree, space="    ", level=0)

    # Write to file (without XML declaration to match example output)
    tree.write(filename, encoding='utf-8', xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): Input XML filename

    Returns:
        dict: Dictionary with string keys and string values
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary from child elements
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
