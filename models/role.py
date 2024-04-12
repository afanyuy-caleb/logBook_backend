import sqlite3 as sq

class Role:
  
  dbfile = 'logBook.db'
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
  
  def update(self, updateData, condition):
    try:
      with sq.connect(Role.dbfile) as conn:
        cur = conn.cursor()

        query = f"UPDATE {Role.table} set {updateData} WHERE {condition}"

        cur.execute(query)
        conn.commit()

        conn.close()

        return True, ''
    
    except sq.Error as err:
      return False, err
  
  def read(self, condition=None):
    try:
       with sq.connect(Role.dbfile) as conn:
        cur = conn.cursor()

        if condition is None:
          query = f"SELECT * FROM {Role.table}"
        else:
          query = f"SELECT * FROM {Role.table} WHERE {condition}"

        cur.execute(query)
        result =  cur.fetchall()

        return True, result
    
    except sq.Error as e:
      return False, e
  
  def delete(self, condition):
    try:
       with sq.connect(Role.dbfile) as conn:
        cur = conn.cursor()
     
        query = f"DELETE FROM {Role.table} WHERE {condition}"
        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as e:
      return False, e