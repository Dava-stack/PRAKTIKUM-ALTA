import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
        UPDATE TBCars SET
          price = 50000
        WHERE   
            id = 101
            """)
print(k.fetchall())

connect_to_db.commit()
connect_to_db.close()