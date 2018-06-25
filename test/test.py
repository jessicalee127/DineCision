from app.DineCision import yelprequest
from app.ui import app
from app.ui import index, error, confirm, yelp
from flask import Flask, url_for
import pytest
import os

API_KEY = os.environ["DINECISION_API_KEY"]
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'


def test_yelprequest():
    url_params = {
        'location': "3+times+square",
        'radius': 500,
        'is_closed': "false",
        'rating': 4,
        'limit': 1,
        'categories': "restaurants, All",
        'price': 2}
    result = yelprequest('https://api.yelp.com', '/v3/businesses/search', API_KEY, url_params)
    result = result["businesses"][0]["id"]
    assert result == "22nKUyCIbpnzR6R3_g1ptQ"

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert "Pick the most exciting place to dine in for you" in str(response.data)

def test_error(client):
    response = client.get('/error')
    assert "You have encountered below error. Please go back and try again" in str(response.data)

def test_confirm(client):
    response = client.get('/confirm/times+square')
    assert "Here is our pick for you:" in str(response.data)

def test_yelp():
    location_input = "times square"
    result = yelp(location_input)
    result = result["id"]
    test_list = ["U5hCNNyJmb7f3dmC1HTzSQ", "22nKUyCIbpnzR6R3_g1ptQ", "DoSU8IPq-Py_YV3kYmXPfQ", "al9HKZ3kCJipAJW4uxzj4A", "5TX0X8w5ssIACU_pnBEq6g"]
    assert result in test_list
