# DineCision

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
