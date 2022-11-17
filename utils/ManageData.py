# import pymysql
# from dotenv import load_dotenv
# import os
import sqlite3

conn = sqlite3.connect("SSCC.db", check_same_thread=False)

cur = conn.cursor()

# STAMP, TEMP, PH, WATER_LEV, LIGHT_LEV, LAST_FEED, PLANT_HEIGHT, PLANT_WIDTH)
conn.execute(
    'CREATE TABLE IF NOT EXISTS AQUA_PONICS_TB (ID INTEGER PRIMARY KEY AUTOINCREMENT, TIMESTAMP TEXT, TEMP FLOAT, PH FLOAT, WATER_LEVEL INT, LED INT, FEED INT)')




# conn.commit()
# conn.close()

# load_dotenv()
#
# DB_USER = os.environ.get('DB_USER')
# DB_PW = os.environ.get('DB_PW')
#
# conn = pymysql.connect(host='127.0.0.1', user=DB_USER, password=DB_PW, db='PURUN', charset='utf8')
# sql = conn.cursor()
#
# def SelectData(query):
#     if query == "":
#         sql.execute(f"SELECT * FROM PURUN_TB")
#     else:
#         sql.execute(f"SELECT * FROM PURUN_TB WHERE {query}")
#     return sql.fetchall()
#
# def InsertData(data):
#     sql.execute(f"INSERT INTO PURUN_TB (STAMP, TEMP, PH, WATER_LEV, LIGHT_LEV, LAST_FEED, PLANT_HEIGHT, PLANT_WIDTH) VALUES ({data})")
#     conn.commit()


def SelectData(query):
    # return f"get {query}"
    cur.execute(f"SELECT * FROM AQUA_PONICS_TB")
    return len(cur.fetchall())

def InsertData(data):
    cur.execute(
        'INSERT INTO AQUA_PONICS_TB (TIMESTAMP, TEMP, PH, WATER_LEVEL, LED, FEED) VALUES (?, ?, ?, ?, ?, ?)',
        ('now', 0.0, 1.0, 128, 0, 1)
    )
    conn.commit()

    return f"insert {data}"
