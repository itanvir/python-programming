import pandas as pd
import sqlite3

# Load dataframe from csv
df = pd.read_csv('/Users/itanvir/Downloads/opm_verification.csv')
df['startdatetime'] = pd.to_datetime(df['startdatetime'])

# Create your connection.
conn = sqlite3.connect("opm.db")

# To sql
df.to_sql('table_name', conn, if_exists='replace', index=False)

# Test
df_test = pd.read_sql('select * from table_name', conn)