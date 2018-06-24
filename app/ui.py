from flask import Flask, request, render_template, flash, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from app.DineCision import yelprequest
from flask_wtf import FlaskForm
import random
import json
import os

API_KEY = os.environ.get("DINECISION_API_KEY") or "Please obtain a Yelp API Key and set it as an environment variable named 'DINECISION_API_KEY'"
SECRET_KEY = os.environ.get("SECRET_KEY") or "my super secret"

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

app = Flask(__name__)
app.secret_key = SECRET_KEY

class NameForm(Form):
    location = TextField('location:', validators=[validators.required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    form = NameForm(request.form)
    if request.method == 'POST' and 'location' in request.form:
        if form.validate():
            return redirect(url_for('confirm', location=request.form.get('location')))
        else:
            flash("Please enter a location")
            return redirect(url_for('error'))
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/confirm/<location>')
def confirm(location):
    random_business = yelp(location)
    if random_business is None:
        flash("Sadly there is no good restaurant to recommend in this location due to limited data, please choose another location")
        return redirect(url_for('error'))
    else:
        return render_template('confirm.html', random_business=random_business['name'], where_is_it_0=random_business["location"]['display_address'][0], where_is_it_1=random_business["location"]['display_address'][1], number_review=random_business["review_count"], pic_url=random_business["image_url"])


def yelp(location_input):

    url_params = {
        'location': location_input.replace(' ', '+'),
        'radius': 500,
        'is_closed': "false",
        'rating': 4,
        'limit': 5,
        'categories': "restaurants, All",
        'price': 2
    }

    result = yelprequest(API_HOST, SEARCH_PATH, API_KEY, url_params)
    business_list = result["businesses"]
    try:
        random_business = random.choice(business_list)
        return random_business
    except IndexError:
        return None


if __name__ == "__main__":
    app.debug = True
    app.run()
