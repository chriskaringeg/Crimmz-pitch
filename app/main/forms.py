from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = TextAreaField("Go", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("Mistari", "Mistari"),("Less entertaining","Less entertaining"),("Humourous","Humourous"),("promotion","promotion"),("product","product"),("Challenging","Challenging"),("random","random")],validators = [Required()]
    )
    submit = SubmitField("Add pitch")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")
    
class EditBio(FlaskForm):
    bio = StringField("Bio")
    submit = SubmitField("Update")
