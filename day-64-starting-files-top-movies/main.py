from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,HiddenField
from wtforms.validators import DataRequired
import requests,os,dotenv

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
dotenv.load_dotenv()
# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
# initialize the app with the extension
db.init_app(app)

  

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String,unique=True,nullable=False)
    year: Mapped[str]=mapped_column(String,nullable=False)
    description: Mapped[str]=mapped_column(String,nullable=False)
    rating: Mapped[float]=mapped_column(Float,nullable=False)
    ranking: Mapped[int]=mapped_column(Integer,nullable=False)
    review: Mapped[str]=mapped_column(String,nullable=False)
    img_url: Mapped[str]=mapped_column(String,nullable=False)

with app.app_context():
    db.create_all()  

class MyForm(FlaskForm):
    id = HiddenField("ID")
    rating = StringField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review  = StringField(u'Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovies(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit=SubmitField('Add Movie')




@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    form=MyForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
            movie.rating = form.rating.data
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home')) 
    return render_template("edit.html", form=form,movie=movie)
    
@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add',methods=["GET", "POST"])
def add():
    form=AddMovies()
    if form.validate_on_submit():
        movie=form.title.data
        response=requests.get('https://api.themoviedb.org/3/search/movie',params={
            'api_key': os.getenv('MOVIE_API'),
            'query': movie,
            'language': 'en-US',
            'page': 1,
            'include_adult': 'false'
        })
        data=response.json()
        if data:
            return render_template('select.html',movies=data['results'])
    return render_template("add.html",form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience 
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": os.getenv('MOVIE_API'), "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"],
            rating=data["vote_average"],
            review="",
            ranking=''

        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))
    
    
if __name__ == '__main__':
    app.run(debug=True)
