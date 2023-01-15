import pandas as pd
from pathlib import Path

csvpath = Path("../Resources/sales.csv")
sales_dataframe = pd.read_csv(csvpath)
sales_dataframe.head()

