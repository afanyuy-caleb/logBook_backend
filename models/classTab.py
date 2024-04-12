import sqlite3 as sq

class classTab:
  
  dbfile = 'logBook.db'
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
  
  def update(self, updateData, condition):
    try:
      with sq.connect(classTab.dbfile) as conn:
        cur = conn.cursor()

        update_query = f"UPDATE {classTab.table} set {updateData} WHERE {condition}"

        cur.execute(update_query)
        conn.commit()

        conn.close()

        return True, ''
    
    except sq.Error as err:
      return False, err
  
  def read(self, condition=None):
    try:
      with sq.connect(classTab.dbfile) as conn:
        cur = conn.cursor()

        if condition is None:
          query = f"SELECT * FROM {classTab.table}"
        else:
          query = f"SELECT * FROM {classTab.table} WHERE {condition}"

        cur.execute(query)
        result =  cur.fetchall()
        
        return True, result
    
    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()
  
  def delete(self, condition):
    try:
       with sq.connect(classTab.dbfile) as conn:
        cur = conn.cursor()
     
        query = f"DELETE FROM {classTab.table} WHERE {condition}"
        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()