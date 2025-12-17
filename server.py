from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title="My Home Page")

@app.route('/about')
def about():
    name = "Pattharaphon"
    email = "fawd@dwadwa.com"
    mobile = "0987654321"
    age = 50
    return render_template('about.html', title="About Us", name=name, email=email, mobile=mobile, age=age)

@app.route('/favorite_foods')
def favorite_foods():
    title = "Favorite Foods page"
    foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Ice Cream"]
    return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favorite_sports')
def favorite_sports():
    title = "Favorite Sports page"
    sports = ["Football", "Basketball", "Swimming", "Tennis", "Badminton"]
    return render_template('favorite_sports.html', title=title, sports=sports)

@app.route('/favorite_movie')
def favorite_movie():
    title = "Favorite Movies page"
    movies = ["Stranger Things", "The Collection (2009-2012)", "Leatherface 2017", "Friday the 13th", "The Strangers"]
    return render_template('favorite_movie.html', title=title, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)