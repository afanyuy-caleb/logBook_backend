import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from models.classTab import classTab

obj = classTab()

def get_items(cond = None):
  if cond is None:
    return obj.read()
  else:
    return obj.read(cond)