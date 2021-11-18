from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('General','General'),('Religion','Religion'),('Politics','Politics'),('Relationships',' Relationships')],validators=[Required()])
    post = TextAreaField('Your Blog', validators=[Required()],render_kw={'class': 'form-control', 'rows': 7})
    submit = SubmitField('Submit Blog')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Save')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
    
class UpdateBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Your Blog', validators=[Required()],render_kw={'class': 'form-control', 'rows': 7})
    submit = SubmitField('Submit Blog')
