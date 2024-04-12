import sqlite3 as sq
import os, sys

current_dir = os.getcwd()
sys.path.append(current_dir)

from .base_model import *
from .constants import PATH_TO_DB

class Courses(Shared_Model, AbstractBaseModel):
  
  dbfile = PATH_TO_DB
  table = 'courses'

  def __init__(self, id, cname, teacher):
    self.id = id
    self.name = cname
    self.teacher = teacher

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
  

  def read(condition=None):
    try:
      with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        if condition:
          query = f"SELECT * FROM {Courses.table} WHERE {condition}"
          result = cur.execute(query).fetchone()

          file = __class__(id=result[0], cname=result[1], teacher=result[2])

          return True, file
        
        else:

          files = []
          query = f"SELECT * FROM {Courses.table}"
          result = cur.execute(query).fetchall()
          
          for row in result:

            file = __class__(id=row[0], cname=row[1], teacher=row[2])
            files.append(file)

          return True, files
    
    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()
  
  
  def toJSON(self):
    return {
      "id": self.id,
      "name": self.name,
      "teacher": self.teacher
    }
