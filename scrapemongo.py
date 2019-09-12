# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from scrape import scrape

def mongo():
    # Store the entire team collection in a list
    data = scrape()
    
    #print (data)
    #x = input("Stop")

    # Create connection variable
    conn = 'mongodb://localhost:27017'
        
    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)
        
    # Connect to a database. Will create one if not already available.
    db = client.mars_db
        
    # Drops collection if available to remove duplicates
    db.marsdata.drop()
        
    # Creates a collection in the database and inserts two document
        
    db.marsdata.insert_one(data)
