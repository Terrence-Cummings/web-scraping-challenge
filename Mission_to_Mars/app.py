from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars
import datetime

# Create an instance of Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars
newsindex = 0

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = db.mars_info.find_one(sort=[( '_id', pymongo.DESCENDING )])

    #Get the date and time of the scrape from mongodb id
    mongo_id = str(mars_data['_id'])
    mongo_timestamp = mongo_id[0:8]
    timestamp_int = int(mongo_timestamp, 16)
    scrape_date = datetime.datetime.fromtimestamp(timestamp_int).date()
    scrape_time = datetime.datetime.fromtimestamp(timestamp_int).time()

    # Return template and data
    return render_template("index.html", mars=mars_data, date=scrape_date, time=scrape_time, newsindex=newsindex)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    #Do a new Mars data scrape
    mars_data = scrape_mars.scrape_info()

    #Setup connection to mongodb
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    # Select database and collection to use
    mars_info = db.mars_info
    mars_info.insert_one(mars_data)

    # Redirect back to home page
    return redirect("/")

#Route that will load the next news article
@app.route("/morenews")
def morenews():

    global newsindex
    newsindex += 1
    if newsindex>39:
        newsindex=0
    
    return redirect("/")

#Route that will load the most recent news article
@app.route("/latestnews")
def latestnews():
    
    global newsindex
    newsindex = 0
    
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
