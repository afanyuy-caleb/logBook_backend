import sqlite3 as sq

class classCourse:
  
  dbfile = 'logBook.db'
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
  
  def update(self, updateData, condition):
    try:
      
      with sq.connect(classCourse.dbfile) as conn:
        cur = conn.cursor()

        update_query = f"UPDATE {classCourse.table} set {updateData} WHERE {condition}"
        
        cur.execute(update_query)
        conn.commit()
        
        return True, ''
    
    except sq.Error as err:
      return False, err
    
    finally:
      conn.close()
      
  
  def read(self, condition=None):
    try:
       with sq.connect(classCourse.dbfile) as conn:
        cur = conn.cursor()

        if condition is None:
          sel = f"SELECT * FROM {classCourse.table}"
        else:
          sel = f"SELECT * FROM {classCourse.table} WHERE {condition}"

        cur.execute(sel)
        result =  cur.fetchone()

        return True, result
    
    except sq.Error as err:
      return False, err
  
  def delete(self, condition):
    try:
       with sq.connect(classCourse.dbfile) as conn:
        cur = conn.cursor()
     
        query = f"DELETE FROM {classCourse.table} WHERE {condition}"
        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as err:
      return False, err