# Project Planning

## Problem Statement

### Primary User
Indecisive individuals, friends, couples, and coworkers who are looking for a quick way to get restaurant recommendations. The app will save users' time searching through vast amount of restaurant information.

### User Needs Statement
"As a group of individuals, we want to get restaurant recommendations simply and quickly. Searching through all the information and deciding on one restaurant requires some significant effort and usually leads to decision fatigue. Every time we plan to go out and dine, we want to save time at the restaurant planning part by having the app do the decision for us." 

### As-Is Process Description
1. Go to Yelp or Google to search for restaurant near a certain location
2. Set certain search criteria (e.g. cuision, price level, openning hours, etc.)
3. Review a list of restaurants that fit the criteria
4. Discuss within the group
5. Decide on one restaurant

## Information Requirements

### Information Inputs
- location

### Information Outputs
- 1 restaurant recommendations and restaurant details


## Technology Requirements

### APIs and Web Service Requirements

Yelp Fusion API - Business Search 
GET https://api.yelp.com/v3/businesses/search

Source: https://www.yelp.com/developers/documentation/v3/business_search

### Python Package Requirements

This app will use a few python packages:
- `urllib`
- `requests`
- `json`
- `argparse`
- `flask`
- `wtforms`
- `flask_wtf`

### Hardware Requirements

Planning to deploy this app to Heroku as a web app.
