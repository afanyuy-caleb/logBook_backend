import sqlite3 as sq
from shared_model import Shared_Model
from constants import PATH_TO_DB

class Students(Shared_Model):
  
  dbfile = PATH_TO_DB
  table = 'students'

  def table_create(self):
    try:

      with sq.connect(Students.dbfile) as conn:
        cur = conn.cursor()
      
        # Enable foreign key support 
        cur.execute('PRAGMA foreign_keys = ON')

        # Create role table
        query = '''CREATE TABLE IF NOT EXISTS students (
          id INTEGER PRIMARY KEY, 
          name varchar(50) UNIQUE COLLATE NOCASE,
          Dob DATE,
          gender char(2) CHECK(gender IN('M', 'F')),
          Tel varchar(12),
          role_id INTEGER default 2,
          class_id INTEGER,
          FOREIGN KEY(role_id) REFERENCES role(role_id),
          FOREIGN KEY(class_id) REFERENCES role(class_id)
          
        )'''
        cur.execute(query)
        conn.commit()

        conn.close()
        return True, ''
      
    except sq.Error as err:
      return False, err


  def write(self, list):
    try:
      with sq.connect(Students.dbfile) as conn:
        cur = conn.cursor()

        for row in list:
            query = f"INSERT INTO {Students.table} VALUES(?, ?, ?, ?, ?, ?, ?)"
            cur.execute(query, row)
            conn.commit()

        conn.close()
      return True, ''

    except sq.Error as err:
      return False, err
  
 