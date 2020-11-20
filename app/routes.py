from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import CommentForm
from app.models import Car, Post


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/carslist', methods=['GET', 'POST'])
def carslist():
    carlist = Car.query.all()
    cars_brands_set = set([])
    car_brands_info = []

    for car in carlist:
        cars_brands_set.add(car.carbrand)

    for brand in cars_brands_set:
        car_brands_info.append(Car.query.filter_by(carbrand=brand).all())

    return render_template('carslist.html', title='Brands', cars_brands_set=cars_brands_set, car_brands_info=car_brands_info)

@app.route('/car/<carname>', methods=['GET', 'POST'])
def car(carname):
    car = Car.query.filter_by(carname=carname).first_or_404()
    form = CommentForm()

    if form.validate_on_submit():
        print(form.comment.data, form.username.data)
        post = Post(name=form.username.data, body=form.comment.data, author=car)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('car', carname=carname))

    posts = car.posts.all()

    return render_template('car2.html', title='Car2', car=car, posts=posts, form=form, carname=carname)


@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
    return render_template('clubs.html')