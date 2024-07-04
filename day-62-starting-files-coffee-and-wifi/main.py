from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location=StringField('Cafe Location on Google Maps(URL)',validators=[DataRequired(),URL()])
    open_time=StringField('Opening time e.g.8am',validators=[DataRequired()])
    close_time=StringField('Closing time e.g.5:30pm',validators=[DataRequired()])
    coffee_rating=SelectField('Rating', choices=[('☕️'),('☕️☕️'),('☕️☕️☕️'),('☕️☕️☕️☕️'),('☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi_rating=SelectField('Rating', choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),("💪💪💪💪💪")], validators=[DataRequired()])
    power_rating=SelectField('Rating', choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),("🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        try:
            with open('day-62-starting-files-coffee-and-wifi\cafe-data.csv', 'a', newline='',encoding='utf-8') as file:
                file.write(f"{form.cafe.data},{form.cafe_location.data},{form.open_time.data},{form.close_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}\n")
            return render_template('index.html', message="Cafe added successfully!")
        except Exception as e:
            return render_template('add.html', form=form, error=f"Error saving cafe data: {e}")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day-62-starting-files-coffee-and-wifi\cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows,length=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
