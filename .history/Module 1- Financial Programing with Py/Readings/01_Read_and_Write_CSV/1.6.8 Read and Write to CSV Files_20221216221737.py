import csv 
from pathlib import Path

csvpath = Path("Module 1- Financial Programing with Py/Readings/01_Read_and_Write_CSV/quarterly_data.csv")
with open(csvpath) as csvfile:
  print(csvfile)





