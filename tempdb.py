import sqlite3 as sqlite
    
database = sqlite.connect("tempy.db")

def data_write(time, int_temp, ext_temp):    
    with database:
        cursor = database.cursor()
        cursor.execute("INSERT INTO data (TIME, INTTEMP, EXTTEMP) VALUES (?, ?, ?)",
                       (time, int_temp, ext_temp)
                       )
        database.commit()
        cursor.close()