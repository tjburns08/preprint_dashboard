from paperscraper.get_dumps import biorxiv, medrxiv, chemrxiv
import json
import pandas as pd
import os

def file_exists(file_path):
    """Check if a file exists at the given path."""
    return os.path.isfile(file_path)

# Get the most recent date from each file
def get_most_recent_date(file_path):
    """
    Finds the most recent date in a JSONL file.

    Args:
        file_path: A string representing the path to the JSONL file to be read.

    Returns:
        A string containing the most recent date in the file, or None if no dates are found.
    """
    most_recent_date = None
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            try:
                data = json.loads(line.strip())
                date = data.get('date')  # Assuming the date field is named 'date'
                if date and (most_recent_date is None or date > most_recent_date):
                    most_recent_date = date
            except json.JSONDecodeError:
                # Ignore lines that can't be parsed as JSON
                continue

    return most_recent_date

def read_and_concatenate_jsonl(file_paths):
    """
    Reads and concatenates JSONL files.

    Args:
        file_paths (list): List of file paths to read and concatenate.

    Returns:
        list: Concatenated lines from all files.
    """
    all_lines = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            all_lines.extend(file.readlines())
    return all_lines

def save_jsonl(data, file_path):
    """
    Saves data to a JSONL file.

    Args:
        data (list): Data to be saved.
        file_path (str): File path for the output file.
    """
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line)

# The whole thing
chem_date = get_most_recent_date('data/latest/chemrxiv.jsonl') if file_exists('data/latest/chemrxiv.jsonl') else None
med_date = get_most_recent_date('data/latest/medrxiv.jsonl') if file_exists('data/latest/medrxiv.jsonl') else None
bio_date = get_most_recent_date('data/latest/biorxiv.jsonl') if file_exists('data/latest/biorxiv.jsonl') else None

# File paths
chem_files = [f for f in ['data/latest/chemrxiv.jsonl', 'data/latest/chemrxiv_tmp.jsonl'] if file_exists(f)]
bio_files = [f for f in ['data/latest/biorxiv.jsonl', 'data/latest/biorxiv_tmp.jsonl'] if file_exists(f)]
med_files = [f for f in ['data/latest/medrxiv.jsonl', 'data/latest/medrxiv_tmp.jsonl'] if file_exists(f)]

# Process and save files
if chem_files:  # Only process if there are files
    chemrxiv = read_and_concatenate_jsonl(chem_files)
    save_jsonl(chemrxiv, 'data/latest/chemrxiv.jsonl')

if bio_files:
    biorxiv = read_and_concatenate_jsonl(bio_files)
    save_jsonl(biorxiv, 'data/latest/biorxiv.jsonl')

if med_files:
    medrxiv = read_and_concatenate_jsonl(med_files)
    save_jsonl(medrxiv, 'data/latest/medrxiv.jsonl')
