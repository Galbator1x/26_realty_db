# Real Estate Site

This board real estate adverts. Implemented filtering by price, region, new buildings.
Ads in json format downloaded through script to the database.

## Installation

```
$ pip install -r requirements.txt
$ . dev.env
$ python
from server import db, app
with app.app_context():
    db.create_all()
```

## Usage

For run site on localhost:
```
python server.py
```
To download ads in database, set 'AdsPath' in file config.ini to ads in json format (default: ads.json).
And run:
```
$ python load_ads_in_db.py
```

## Requirements

- Python >= 3.5

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
