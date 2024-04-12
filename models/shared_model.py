import sqlite3 as sq
from constants import PATH_TO_DB

class Shared_Model:
  
  def update(self, updateData, condition, tableName):
    try:
      with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        update_query = f"UPDATE {tableName} set {updateData} WHERE {condition}"

        cur.execute(update_query)
        conn.commit()

        conn.close()

        return True, ''
    
    except sq.Error as err:
      return False, err
  
  def read(self, tableName, condition=None ):
    try:
      with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        if condition is None:
          query = f"SELECT * FROM {tableName}"
        else:
          query = f"SELECT * FROM {tableName} WHERE {condition}"

        cur.execute(query)
        result =  cur.fetchall()
        
        return True, result
    
    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()
  
  def delete(self, tableName, condition):
    try:
       with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()
     
        query = f"DELETE FROM {tableName} WHERE {condition}"
        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()