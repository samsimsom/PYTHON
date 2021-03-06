

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TweetForm(FlaskForm):
    tweet = StringField('Tweet',
                        validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('submit')
