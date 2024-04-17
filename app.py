import os
from flask import Flask, send_from_directory

from views.courses import courses_view
from views.students import students_view

app = Flask(__name__)

app.register_blueprint(courses_view)
app.register_blueprint(students_view)
