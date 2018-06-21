# DineCision

## Installation

Install source code:

```sh
git clone https://github.com/jessicalee127/DineCision.git
cd DineCision/
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

Obtain a Yelp API Key and store the result in an environment variable called `DINECISION_API_KEY`.

## Usage

Run the app locally:

```sh
FLASK_APP=app FLASK_ENV=development flask run
```
