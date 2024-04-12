import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from models.class_courses import classCourse
import views.shared_data as shared

import json
obj = classCourse()

def add_course_Info(date, desc = None, img = None, cour_id = None):

  if shared.studInfo:
    studData = shared.studInfo

    if date == "":
      return False, 'Please enter the date'
    else:
      if not desc and not img:
        return False, "Either description or the image must be provided"
    
    # Convert the information into a json
    courseInfo_Dict = {}

    courseInfo_Dict['date'] = date
    courseInfo_Dict['desc'] = desc
    courseInfo_Dict['img'] = img

    cond = f"course_id = {cour_id} AND class_id = {studData['class_id']}"
    stat, data = obj.read(cond)

    if stat:
      if data[2] is None:
        infoList = []
        
      else:
        infoList = json.loads(data[2])
      
      infoList.append(courseInfo_Dict)
      json_info = json.dumps(infoList)

      # update the DB
      update_data = f"course_info = '{json_info}'"
      update = obj.update(update_data, cond)
      if update[0]:
        pass

      else:
        print("Error, due to: ", update[1])

    else:
      print("Error: ", data[0])
    
    return True, 'Course Info added successfully'

  else:
    return False, "Theres nothing there"

