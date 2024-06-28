from flask import Flask, render_template,request
import requests,os,dotenv
from smtplib import SMTP

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
dotenv.load_dotenv()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact",methods=['POST'])
def received_data():
    name=request.form.get('name')
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')
    with SMTP(host='smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv('SMPT_SENDER'),password=os.getenv('SMTP_PASSWORD'))
        connection.sendmail(from_addr=os.getenv('SMPT_SENDER'),to_addrs=os.getenv('SMTP_RECEIVER'),
                msg=f"""
                name: {name} \n
                email: {email} \n
                phone: {phone} \n
                message: {message} \n
                """)
        connection.close()
    return render_template('contact.html',string="Successfully sent message")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
