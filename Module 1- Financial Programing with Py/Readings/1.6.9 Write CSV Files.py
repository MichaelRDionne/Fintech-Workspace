import csv
from pathlib import Path

data = [
    {
        "first_name": "Jericho",
        "last_name": "Smith",
        "pin": 123
    },
    {
        "first_name": "Samantha",
        "last_name": "Jones",
        "pin": 456
    }
]

header = ["first_name", "last_name", "pin"]

csvpath = Path("my_output.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write our header row first!
    csvwriter.writerow(header)

    # Then we can write the data rows
    for row in data:
        csvwriter.writerow(row.values())
        