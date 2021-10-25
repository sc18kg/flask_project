from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class AddTask(FlaskForm):
    
    task_title = SelectField("Task Title:",choices=[],
        validators=[ Length(min=1, message="The film title field can't be empty!")])
    module = StringField("Module Code:")
    desc = StringField("Description:")
    deadline = StringField("Deadline Date:")
    complete = 
    submit = SubmitField("Add Task")