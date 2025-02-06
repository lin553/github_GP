import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('./pandas库/008.00.db')
cur = conn.cursor()
try:
    sql = """CREATE TABLE table_name (
                id integer primary key autoincrement,
                coin_name varchar(15) not null,
                low integer,
                avg integer,
                high integer,
                c_time integer
            );"""
    cur.execute(sql)
    print("create table success")
    # return  True
except OperationalError as o:
    print(str(o))
    pass
    if str(o) == "table table_name already exists":
        pass
        # return True
    # return False
except Exception as e:
    print(e)
    # return False
finally:
    cur.close()
    conn.close()