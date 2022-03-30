from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, StringField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = IntegerField('Teamlead id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is finished')
    submit = SubmitField('Submit')
