from flask import Flask, render_template, jsonify, redirect
import pymongo
from scrapemongo import mongo

app = Flask(__name__, static_url_path='/static')

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
#marsdata = db.marsdata

@app.route("/scrape")
def scrape():

    mongo()
    
    #return jsonify("Finished - Press Back in Browser")
    
    data = db.marsdata.find()
    for d in data:
        data1 = d

    # render an index.html template and pass it the data you retrieved from the database
    #return render_template("index.html", dict=data1)
    return redirect("/")
    #return jsonify("Press back to return")
    #return redirect("http://www.example.com", code=302)


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    data = db.marsdata.find()
    for d in data:
        data1 = d

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", dict=data1)


if __name__ == "__main__":
    app.run(debug=True)