import sqlite3 as sq
from shared_model import Shared_Model
from constants import PATH_TO_DB

class Role(Shared_Model):
  
  dbfile = PATH_TO_DB
  table = 'role'

  def create(self):
    try:

      with sq.connect(Role.dbfile) as conn:
        cur = conn.cursor()
      
        # Create role table
        query = f"CREATE TABLE IF NOT EXISTS {Role.table} (role_id INTEGER PRIMARY KEY, role_name varchar(15) UNIQUE)"

        cur.execute(query)
        conn.commit()

        conn.close()
        return True, ''
      
    except sq.Error as err:
      return False, err


  def write(self, list):
    try:
      with sq.connect(Role.dbfile) as conn:
        cur = conn.cursor()

        for row in list:
          query = f"INSERT INTO {Role.table} (role_id, role_name) VALUES (?, ?)"
          cur.execute(query, row)
          conn.commit()

        conn.close()
      return True, ''

    except sq.Error as err:
      return False, err
