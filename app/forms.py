from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Optional

class CourseForm(FlaskForm):
    """Form for adding and editing courses"""
    course_code = StringField('Course Code', 
                           validators=[
                               DataRequired(),
                               Length(min=2, max=20, message='Course code must be between 2 and 20 characters')
                           ],
                           render_kw={"placeholder": "e.g., CS101", "class": "form-control form-control-lg"})
    
    course_name = StringField('Course Name',
                            validators=[
                                DataRequired(),
                                Length(min=5, max=100, message='Course name must be between 5 and 100 characters')
                            ],
                            render_kw={"placeholder": "e.g., Introduction to Computer Science", "class": "form-control form-control-lg"})
    
    submit = SubmitField('Save Course', render_kw={"class": "btn btn-primary px-4"})
    action = HiddenField('action')
    course_id = HiddenField('course_id')
