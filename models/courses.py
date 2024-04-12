import sqlite3 as sq

class Courses:
  
  dbfile = 'logBook.db'
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
  
  def update(self, updateData, condition):
    try:
      with sq.connect(Courses.dbfile) as conn:
        cur = conn.cursor()

        update_query = f"UPDATE {Courses.table} set {updateData} WHERE {condition}"

        cur.execute(update_query)
        conn.commit()

        conn.close()

        return True, ''
    
    except sq.Error as err:
      return False, err
  
  def read(self, condition=None):
    try:
       with sq.connect(Courses.dbfile) as conn:
        cur = conn.cursor()

        if condition is None:
          sel = f"SELECT * FROM {Courses.table}"
        else:
          sel = f"SELECT * FROM {Courses.table} WHERE {condition}"

        cur.execute(sel)
        result =  cur.fetchall()

        return True, result
    
    except sq.Error as e:
      return False, e
  
  def delete(self, condition):
    try:
       with sq.connect(Courses.dbfile) as conn:
        cur = conn.cursor()
     
        query = f"DELETE FROM {Courses.table} WHERE {condition}"
        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as err:
      return False, err