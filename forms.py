from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from wtforms.fields.html5 import EmailField


# ----- SIGN UP FORM ----- #
class RegisterForm(FlaskForm):
    email = EmailField("Email address", [
        validators.DataRequired(), validators.Email()
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    name = StringField("Name", [validators.Length(min=4, max=25)])
    submit = SubmitField("Register")


# ----- LOGIN FORM ----- #
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# ----- CREATE POST FORM ----- #
class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("What's on your mind...", validators=[DataRequired()])
    submit = SubmitField("Publish")


# ----- COMMENT FORM ----- #
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
