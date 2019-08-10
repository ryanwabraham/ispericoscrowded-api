# Is Pericos Crowded API

### Intro
Hello Pericos fam! This code represents the API endpoint that powers [ispericoscrowded.com](https://ispericoscrowded.com).
It is written using Python 3 and is run on an AWS Lambda. It uses the serverless framework for deployments.

### How does it work?
It is powered by the populartimes library written by [@m-wrzr](https://github.com/m-wrzr), which uses the Google Places API, anonymous GPS data from smartphones, and some web scraping magic to determine how busy a place currently is.

When a client does a GET on this endpoint, it will receive this data in JSON format.
