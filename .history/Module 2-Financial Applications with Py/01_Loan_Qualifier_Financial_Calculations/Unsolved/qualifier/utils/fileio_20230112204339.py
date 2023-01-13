"""Helper functions to load CSV data."""

import csv

def load_csv(csvpath):
    """Reads rhe CSV file from the path provided."""
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
