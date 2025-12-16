from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="My Home Page")

@app.route('/about')
def about():
    name = "Pattharaphon"
    email = "fawd@dwadwa.com"
    mobile = "0987654321"
    age = 50
    return render_template('about.html', title="About Us", name=name, email=email, mobile=mobile, age=age)

@app.route('/faverite/food')
def faverite_food():
    title = "Favorite Foods page"
    foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Ice Cream"]
    return render_template('faverite_foods.html', title=title, foods=foods)

@app.route('/faverite/sport')
def faverite_sport():
    title = "Favorite sport page"
    sports = ["Football", "Basketball", "Swimming", "Tennis", "Badminton"]
    return render_template('faverite_sport.html', title=title, sports=sports)

if __name__ == '__main__':
    app.run(debug=True)