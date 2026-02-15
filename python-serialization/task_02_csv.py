#!/usr/bin/python3
"""Module to convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and saves to data.json.

    Args:
        csv_filename (str): Path to the input CSV file

    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    try:
        # Read CSV data using DictReader (converts rows to dictionaries)
        with open(csv_filename, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)  # Convert iterator to list of dictionaries

        # Write JSON data to data.json with pretty formatting
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # Handle missing CSV file
        return False
    except Exception:
        # Handle any other errors (corrupted CSV, write permissions, etc.)
        return False
