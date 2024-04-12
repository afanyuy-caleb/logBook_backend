from flask import Blueprint, request
import os, sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from controllers.coursectrl import *
from utils import parse_request_data
from responses import JSONResponse

courses_view = Blueprint('courses', __name__, url_prefix='/courses')

@courses_view.route('/', methods=['GET', 'POST'])
def list_or_create():
  if request.method == 'GET':
    return get_items()
  
  else:
    submitted_data = parse_request_data(request=request)

    
