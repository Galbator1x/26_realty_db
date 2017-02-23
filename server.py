from models import db, Ad

from datetime import date
import os

from flask import Flask, render_template, current_app, request

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route('/', methods=['GET'])
def ads_list():
    ads = Ad.query.filter(Ad.active == True)
    district = request.args.get('oblast_district')
    min_price = request.args.get('min_price', None, type=int)
    max_price = request.args.get('max_price', None, type=int)
    new_building = request.args.get('new_building')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if district:
        ads = ads.filter(Ad.oblast_district == district)
    if min_price:
        ads = ads.filter(Ad.price >= min_price)
    if max_price:
        ads = ads.filter(Ad.price <= max_price)
    if new_building:
        ads = ads.filter(Ad.under_construction == True or
                         Ad.construction_year >= date.today().year - 2)

    ads = ads.paginate(page, per_page, False)
    return render_template('ads_list.html',
            ads=ads,
            district=district,
            min_price=min_price,
            max_price=max_price,
            new_building=new_building,
            cities=sorted(current_app.config['CITIES'],
                key=lambda city: city[1]))


if __name__  ==  '__main__':
    app.run()
