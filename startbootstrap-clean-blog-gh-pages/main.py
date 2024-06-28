from flask import Flask,render_template
import requests

app=Flask(__name__)


@app.route("/")
def home():
    response=requests.get('https://api.npoint.io/f5283c323894a2ab9b05').json()
    return render_template('index.html',blog_posts=response)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<num>')
def get_post(num):
    response=requests.get('https://api.npoint.io/f5283c323894a2ab9b05').json()
    return render_template('post.html',blog_posts=response,num=int(num))


if __name__=="__main__":
    app.run(debug=True)