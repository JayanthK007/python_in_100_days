from flask import Flask,render_template
import random,datetime
import requests


app=Flask(__name__)

@app.route("/")
def home():
    random_num=random.randint(0,9)
    return render_template('index.html',num=random_num,date=datetime.date.today().year)

@app.route("/guess/<name>")
def guess(name):
    # Fetch gender data
    gender_response = requests.get('https://api.genderize.io', params={"name": name})
    if gender_response.status_code == 200:
        gender_data = gender_response.json()
        gender = gender_data.get('gender')
    else:
        gender = None
    
    # Fetch age data
    age_response = requests.get('https://api.agify.io', params={"name": name})
    if age_response.status_code == 200:
        age_data = age_response.json()
        age = age_data.get('age')
    else:
        age = None
    
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blogs=requests.get("https://api.npoint.io/6ffe7bb48be13de7e83b").json()
    return render_template('blog.html', blogs=blogs)


if __name__=="__main__":
    app.run(debug=True)