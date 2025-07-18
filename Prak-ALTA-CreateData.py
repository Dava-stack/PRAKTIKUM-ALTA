import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
    INSERT INTO TBCars (
          id,
          name,
          brand,
          model,
          price
          )
          VALUES ('101','BMW F30','BMW','F30',20000),
                 ('102','BMW F10','BMW','F10',25000)
          )
          """)

connect_to_db.commit()
connect_to_db.close()