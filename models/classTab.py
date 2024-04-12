import sqlite3 as sq
from constants import PATH_TO_DB
from shared_model import Shared_Model

class classTab (Shared_Model):
  
  dbfile = PATH_TO_DB
  table = 'class'

  def table_create(self):
    try:

      with sq.connect(classTab.dbfile) as conn:
        cur = conn.cursor()
      
        # Create the class table
        query = "CREATE TABLE IF NOT EXISTS class (class_id INTEGER PRIMARY KEY, class_name varchar(15) UNIQUE)"
        cur.execute(query)
        conn.commit()

        conn.close()
        return True, ''
      
    except sq.Error as err:
      return False, err


  def write(self, list):
    try:
      with sq.connect(classTab.dbfile) as conn:
        cur = conn.cursor()

        for row in list:
            query = f"INSERT INTO {classTab.table} VALUES(?, ?)"
            cur.execute(query, row)
            conn.commit()

        conn.close()
      return True, ''

    except sq.Error as err:
      return False, err

# obj.read()


