from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
#import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    #mars_data = mongo.db.collection.find_one()

    mars_data = {
        'article':[
            {'date':'May 21, 2020', 'title':"Air Deliveries Bring NASA's Perseverance Mars Rover Closer to Launch", 'summary':"A NASA Wallops Flight Facility cargo plane transported more than two tons of equipment — including the rover's sample collection tubes — to Florida for this summer's liftoff."},
            {'date':'May 19, 2020', 'title':"NASA Wins 4 Webbys, 4 People's Voice Awards", 'summary':"Winners include the JPL-managed Send Your Name to Mars campaign, NASA's Global Climate Change website and Solar System Interactive."}
        ],
        'weather': 'InSight sol 529 (2020-05-22) low -93.2ºC (-135.8ºF) high 0.6ºC (33.1ºF), winds from the WNW at 4.6 m/s (10.3 mph) gusting to 15.5 m/s (34.6 mph), pressure at 7.10 hPa',
        'featured_image': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23170_hires.jpg',
        'mars_facts': 'facts test',
        'mars_hems': [
            {'title': 'Cerberus Hemisphere','img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
            {'title': 'Schiaparelli Hemisphere','img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
            {'title': 'Syrtis Major Hemisphere','img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
            {'title': 'Valles Marineris Hemisphere','img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}
        ]
    }

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
