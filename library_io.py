"""
Library I/O Module
Copyright 2025, Surbhi Sharma
"""
import json
import os

LIBRARY_FILE = 'library_data.json'  # File to store library data

def load_library():
    """
    Load library data from the file.
    If the file does not exist, return an empty dictionary.
    """
    if not os.path.exists(LIBRARY_FILE):
        return {}  # Return an empty dictionary if the file does not exist

    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading library data: {e}")
        return {}

def save_library(library):
    """
    Save the current library data to the file in JSON format.
    """
    try:
        with open(LIBRARY_FILE, 'w') as file:
            json.dump(library, file)
    except Exception as e:
        print(f"Error saving library data: {e}")
