import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from models.students import Students

obj = Students()

def load(cond = None):
  if cond is None:
    return obj.read()
  else:
    return obj.read(cond)