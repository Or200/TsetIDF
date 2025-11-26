import sqlite3, pandas as pd

def load_csv_into_db(path):

    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    conn = sqlite3.connect("db\soldiers.db")
    df.to_sql("soldiers", conn, if_exists="replace", index=False)
    my_cursor = conn.cursor()
    conn.close()

    conn = sqlite3.connect("db/rooms.db")
    my_cursor = conn.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS room(id INTEGER, assignment_status text NOT NULL, dorm text, room_num text)")
    conn.close()


