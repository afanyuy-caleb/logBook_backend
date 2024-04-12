import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from models.courses import Courses

TABLE_NAME = 'courses'

def get_items(cond = None, return_obj=False):

  if cond is None:
    courses = Courses.read()

    if not return_obj:
      list_of_courses = [
        course.toJSON() for course in courses
      ]
      return list_of_courses
    
    return courses

  else:
    course = Courses.read(cond)
  
    return course if return_obj else course.toJSON()
    

