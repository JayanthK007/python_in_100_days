from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Email()])
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField('Log In')



app = Flask(__name__)
bootstrap=Bootstrap5(app)

app.config['SECRET_KEY'] = 'any secret string'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'admin@email.com' and password == '12345678':
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')



@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
