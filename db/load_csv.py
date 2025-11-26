import sqlite3, pandas as pd

def load_csv_into_db():

    df = pd.read_csv("csv\soldiers.csv")
    df.columns = df.columns.str.strip()
    conn = sqlite3.connect("db\soldiers.db")
    df.to_sql("soldiers", conn, if_exists="replace", index=False)
    conn.close()


load_csv_into_db()







# def Load_CSV_into_DB(mydb: mysql.connector):
    
#     mycursor = mydb.cursor()

#     mycursor.execute("CREATE TABLE IF NOT EXISTS courses (id INT AUTO_INCREMENT PRIMARY KEY, institution VARCHAR(255) NOT NULL, city VARCHAR(255) NOT NULL, address VARCHAR(255), course VARCHAR(255) NOT NULL, district VARCHAR(255), telephone VARCHAR(50), email VARCHAR(255))")
#     mycursor.execute("ALTER TABLE courses AUTO_INCREMENT=1")

#     rows_count = 0

#     with open("./data/courses.csv", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         next(reader)


#         for row in reader:
#             mycursor.execute("INSERT INTO courses (institution, city, address, course, district, telephone, email) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)
#             rows_count += 1

#         mydb.commit()
#         print(f"{rows_count} loaded successfully")

    