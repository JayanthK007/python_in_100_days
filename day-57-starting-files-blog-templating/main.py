from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/blog")
def get_blog():
    blogs=requests.get("https://api.npoint.io/6ffe7bb48be13de7e83b").json()
    return render_template('index.html', blogs=blogs)

@app.route("/post/<num>")
def get_post(num):
    blogs=requests.get("https://api.npoint.io/6ffe7bb48be13de7e83b").json()
    return render_template('post.html', num=num,blogs=blogs[int(num)-1])


if __name__ == "__main__":
    app.run(debug=True)
