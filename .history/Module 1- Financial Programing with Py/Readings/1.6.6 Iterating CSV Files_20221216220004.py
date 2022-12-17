# read & write data to files
# CSV = comma-separated values = spreadsheet format (data)
# CSV has header & rows
# CSV uses delimiters like commas to seperate columns
# CSV uses double quotes to escape values

# needs pathlib Library 

import pathlib
from pathlib import Path

# Now that Path from the pathlib library is imported, you can use it to create a path to the same folder that the code file sits in. In the following code, remember that "." represents the current directory:
my_directory = Path(".")
print(my_directory)

csvpath = Path("data.csv")
print(csvpath)
