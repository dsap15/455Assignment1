from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'

bootstrap = Bootstrap(app)


class OverrideForm(FlaskForm):
    vnumber = StringField('Enter your V-Number(Please enter the leading V and all 8 digits) *', validators=[DataRequired()])
    fullname = StringField('Enter your Full Name (Last Name, First Name) Please do not use nicknames. *', validators=[DataRequired()])
    email = StringField('Enter your VCU Email Address *', validators=[DataRequired()])
    coursenumber = StringField('Enter the Course Number for which you are requesting an override. (For example: STAT 210) *', validators=[DataRequired()])
    sectionnumber = StringField('Enter the Section Number(s) for which you are requesting an override. (For example 001) *', validators=[DataRequired()])
    referencenumber = StringField('Enter the Course Reference Number(s) (CRN) for which you are requesting an override. (For example 16071) *', validators=[DataRequired()])
    reason = StringField('Give the reason why you are requesting the override. (Type a brief description) *', validators=[DataRequired()])
    comment = TextAreaField('Additional Comment- Please provide any additional information which may be useful regarding your request, including how prerequisite is satisfied if prerequisite override request, and issue if other request.', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():

    form = OverrideForm()
    if form.validate_on_submit():
        vnumber = form.vnumber.data
        fullname = form.fullname.data
        email = form.email.data
        coursenumber = form.coursenumber.data
        sectionsumber = form.sectionnumber.data
        referencenumber = form.referencenumber.data
        reason = form.reason.data
        comment = form.comment.data
        return render_template('thanks.html')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
