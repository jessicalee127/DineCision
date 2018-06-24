# DineCision

## Introduction

This app helps individuals, friends, and families with decision fatigue to quickly pick great restaurants to dine in, using simple user search input: location address or zipcode. 

When a restaurant is picked, the result will display the restaurant name, reason why it's recommended, location of the restaurant, and a vivid picture of the food from the restaurant.

Proper error handling has been added to handle scenarios when there is no user input, and when there is not enough restaurant data from the user chosen location.

An example of this app running on Heroku servers can be found here: https://powerful-eyrie-98502.herokuapp.com/


## Installation

Prerequisites: Install Python 3.6.

Install source code:

```sh
git clone https://github.com/jessicalee127/DineCision.git
cd DineCision/ # all commands below assume you are running them from this repository's root directory
```

Install package dependencies:

```sh
pipenv install -r requirements.txt # then run `pipenv shell` before continuing
# or...
pip3 install -r requirements.txt
# or...
pip install -r requirements.txt
```

## Setup

Obtain a [Yelp Fusion API Key](https://www.yelp.com/developers/v3/manage_app) and store the result in an environment variable called `DINECISION_API_KEY`.

## Usage

Run the app locally:

```sh
FLASK_APP=app FLASK_ENV=development flask run
```
Run `DineCision.py` if you wish to run this app via command line only.

Run `ui.py` if you wish to run the GUI version of the app from your localhost.

## Deploying

Prerequisites: register for a [Heroku](https://heroku.com) account, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and login from the command-line (`heroku login`).

One-time, first time only, to provision a new Heroku server:

```sh
heroku create
```

One-time, first time only, to configure environment variables on the server:

```sh
heroku config:set DINECISION_API_KEY="abc123" # where "abc123" is your Yelp API Key
```

Subsequent times, to deploy:

```sh
git push heroku master
```
