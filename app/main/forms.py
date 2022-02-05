from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField 
from wtforms.validators import InputRequired

class ReviewForm(FlaskForm):

  title= StringField('Review title', validators=[InputRequired()])
  review = TextAreaField('Movie Review')
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us abou you', validators=[InputRequired()])
  submit = SubmitField('submit')