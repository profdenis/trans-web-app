from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectMultipleField, RadioField, SelectField
from wtforms.fields import EmailField, DateField, IntegerField
from wtforms.validators import InputRequired, Email, Length, Regexp, ValidationError, NumberRange
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms_components import ColorField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Message', validators=[InputRequired()], render_kw={'rows': 10})
    submit = SubmitField('Send')


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class ExamplesForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(),
                                       Length(4, 64),
                                       Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must start with a letter and must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[InputRequired(), Length(8)])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(1, 125)])
    fav_color = ColorField('Favorite Color', validators=[InputRequired()])
    dob = DateField('Date of birth', validators=[InputRequired()])
    checkbox_group = MultiCheckboxField('Checkbox group',
                                        choices=[('c1', 'Checkbox 1'), ('c2', 'Checkbox 2'), ('c3', 'Checkbox 3')])
    radio_group = RadioField('Radio button group', validators=[InputRequired()],
                             choices=[('r1', 'Radio button 1'), ('r2', 'Radio button 2'), ('r3', 'Radio button 3')],
                             render_kw={'required': True})
    select = SelectField('Drop down select', validators=[InputRequired()],
                         choices=[('o1', 'Option 1'), ('o2', 'Option 2'), ('o3', 'Option 3')])
    submit = SubmitField('Submit')

    def validate_password(self, field):
        with open('data/common_passwords.txt') as f:
            for line in f.readlines():
                if field.data == line.strip():
                    raise ValidationError('Your password is too common.')
