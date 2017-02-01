from server import db, app
from models import Ad

import json
import configparser


def get_path_to_ads():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['AdsPath']


def load_json(path):
    with open(path) as file_handler:
        return json.load(file_handler)


def load_ads_in_db(ads):
    with app.app_context():
        for ad in Ad.query.filter_by(active=True):
            ad.active = False
        for ad in ads:
            _ad = Ad.query.get(ad['id'])
            if _ad is None:
                _ad = Ad()
            _ad.id = ad['id']
            _ad.settlement = ad['settlement']
            _ad.under_construction = ad['under_construction']
            _ad.description = ad['description']
            _ad.price = ad['price']
            _ad.oblast_district = ad['oblast_district']
            _ad.living_area = ad['living_area']
            _ad.has_balcony = ad['has_balcony']
            _ad.address = ad['address']
            _ad.construction_year = ad['construction_year']
            _ad.rooms_number = ad['rooms_number']
            _ad.premise_area = ad['premise_area']
            _ad.active = True
            db.session.add(_ad)
        db.session.commit()


if __name__ == '__main__':
    load_ads_in_db(load_json(get_path_to_ads()))

