from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    age = IntegerField('What is your age?', validators=[NumberRange(min=1, max=200, message='非法范围')])
    submit = SubmitField('Submit')
