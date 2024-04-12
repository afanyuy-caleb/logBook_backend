import sqlite3 as sq
from shared_model import Shared_Model
from constants import PATH_TO_DB

class Courses(Shared_Model):
  
  dbfile = PATH_TO_DB
  table = 'courses'

  def create(self):
    try:

      with sq.connect(Courses.dbfile) as conn:
        cur = conn.cursor()
      
        # Create Courses table
        query = f"CREATE TABLE IF NOT EXISTS {Courses.table} (course_id INTEGER PRIMARY KEY, course_name varchar(15) UNIQUE, teacher varchar(40))"

        cur.execute(query)
        conn.commit()

        conn.close()
        return True, ''
      
    except sq.Error as err:
      return False, err


  def write(self, list):
    try:
      with sq.connect(Courses.dbfile) as conn:
        cur = conn.cursor()

        for row in list:
          insert = f"INSERT INTO {Courses.table} (Courses_id, Courses_name) VALUES (?, ?)"
          cur.execute(insert, row)
          conn.commit()

        conn.close()
      return True, ''

    except sq.Error as err:
      return False, err
  
  