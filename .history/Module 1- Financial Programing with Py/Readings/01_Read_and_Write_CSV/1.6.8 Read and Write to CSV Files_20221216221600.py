import csv 
from pathlib import Path

csvpath = Path("quarterly_data.csv")
with open(csvpath) as csvfile:
  print(csvfile)




