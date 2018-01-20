from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import pymongo
from scrape.py import scrape

app = Flask(__name__)
mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars

@app.route('/')
def index():
    mars_info = collection.find_one()

    return render_template("index.html",mars_info=mars_info)


@app.route('/scrape')
def scrape():
    mars_dict = scrape()
    collection.update({"id":1},{"$set",mars_dict},upsert=True)

    return redirect("http://localhost:5000",code = 302)


if __name__ == "__main__":
    app.run(debug=True)
