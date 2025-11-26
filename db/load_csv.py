import sqlite3, pandas as pd

def load_csv_into_db():

    df = pd.read_csv("csv\soldiers.csv")
    df.columns = df.columns.str.strip()
    conn = sqlite3.connect("db\soldiers.db")
    df.to_sql("soldiers", conn, if_exists="replace", index=False)
    conn.close()
