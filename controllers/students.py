import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from models.students import Students

obj = Students()

def get_items(cond = None, return_obj=False):

  if cond is None:
    status, students = obj.read()

  else:
    status, students = obj.read(cond)

  if status:
    if not return_obj:
      list_of_students = [
        course.toJSON() for course in students
      ]
      return list_of_students
    
    return students

  else:
    return None

def get_unique_item(col, data, return_obj = False):

  status, student = obj.read_unique(column=col, data=data)

  if status and not return_obj:
    return status, student.toJSON

  return status, student

def save_student(item_dict):
  if len(item_dict) > 7 or len(item_dict) < 2 :
    return False, "column count doesn't match"
  
  column_list = ['id', 'name', 'Dob', 'gender', 'Tel', 'role', 'class']

  # Ensure there are no unknown columns
  for key in item_dict.keys():
    if key not in column_list:
      return False, f"Invalid key, {key}"
  
  # Ensure that a unique column is present
  if 'course_id' not in item_dict:
    if 'course_name' not in item_dict:
      return False, "A Unique column must be present"

  # Ensure that the role presented is either
  update = update_id = False
  if 'course_id' in item_dict:
    # Verify if the id exists in the db
    id = item_dict['course_id']
    status, exist_course = get_unique_item(col="course_id", data=id, return_obj=True)

    if status:
      update = update_id = True
      
  if not update:
    if 'course_name' in item_dict:
      # Check for the course_name
      name = item_dict['course_name']
      status, exist_course = get_unique_item(col="course_name", data=name, return_obj=True)

      if status:
        update = True

  if not update:
    # Insert into the db
    return insert(item_dict, column_list)
    
  else:
    # Update the db
    if update_id:
      return update_course(item_dict, "course_id", id)
    
    else:
      return update_course(item_dict, "course_name", name)


def update_course(item_dict, column, unq_value):
  setInfo = ""
  length = 1
  for key, value in item_dict.items():
    if length == len(item_dict):
      setInfo += f"{key} = '{value}' "
    
    else:
      setInfo += f"{key} = '{value}', "

    length += 1

  return obj.update(column, setInfo, unq_value)
    

def insert(dict, col_list):
  for col in col_list:
    if col not in list(dict.keys()):
      dict[col] = None
  
  dict['course_id'] = None

  # sort the keys in db order 
  dict = {key : dict[key] for key in col_list}
  value_tuple = tuple(dict.values())
  
  return obj.write(value_tuple, set_type=True)


def delete_course(item_dict):
  
  if len(item_dict) > 3 :
    return False, "column count doesn't match"
  
  column_list = ['course_id', 'course_name', 'teacher']

  for key in item_dict.keys():
    if key not in column_list:
      return False, f"Invalid key, {key}"
  
  if 'course_id' not in item_dict:
    if 'course_name' not in item_dict:
      return False, "A Unique column must be present"
  
  if 'course_id' in item_dict:
    id = item_dict['course_id']
    condition = f"course_id = {id}"

  else:
    name = item_dict['course_name']
    condition = f"course_name = '{name}'"

  return obj.delete(condition)