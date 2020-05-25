from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import pymongo
#import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = db.mars_info.find_one(sort=[( '_id', pymongo.DESCENDING )])

    # Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
# @app.route("/scrape")
# def scrape():

#     # Run the scrape function
#     mars_data = scrape_mars.scrape_info()

#     # Update the Mongo database using update and upsert=True
#     mongo.db.collection.update({}, mars_data, upsert=True)

#     # Redirect back to home page
#     return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
