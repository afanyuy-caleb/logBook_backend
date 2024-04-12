import sqlite3 as sq
from constants import PATH_TO_DB
from shared_model import Shared_Model

class classCourse(Shared_Model):
  
  dbfile = PATH_TO_DB
  table = 'class_courses'

  def create(self):
    try:

      with sq.connect(classCourse.dbfile) as conn:
        cur = conn.cursor()

        # Enable foreign key support 
        cur.execute('PRAGMA foreign_keys = ON')
      
        # Create the course information table
        query = '''CREATE TABLE IF NOT EXISTS class_courses (
          class_id INTEGER,
          course_id INTEGER,
          course_info TEXT,
          PRIMARY KEY(class_id, course_id)
        )'''
        cur.execute(query)
        conn.commit()

        conn.close()
        return True, ''
      
    except sq.Error as err:
      return False, err


  def write(self, list):
    try:
      with sq.connect(classCourse.dbfile) as conn:
        cur = conn.cursor()

        insert = f"INSERT INTO {classCourse.table} (class_id, course_id, course_info) VALUES (?, ?, ?)"
        cur.execute(insert, list)
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