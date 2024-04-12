import sqlite3 as sq
from constants import PATH_TO_DB
from .base_model import *

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

  def read(self, tableName, condition=None ):
    try:
      with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        if condition:
          query = f"SELECT * FROM {tableName}"
          result = cur.execute(query).fetchone()

          for row in result:
            file = __class__(id=result[0])

            
          
          return True, result
        
        else:
          query = f"SELECT * FROM {tableName} WHERE {condition}"
          result = cur.execute(query).fetchall()
          
          return True, result
    
    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()
# obj.read()


