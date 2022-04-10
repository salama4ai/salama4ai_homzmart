from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
    

class Hotel_Indexer(Resource)
    """the hotel indexer class"""

    def post(self):
        return "<p>Hello, World! hotel_indexer</p>"



BASE = "http://127.0.0.1:9200/"
response = requests.put(BASE + "hotelindexer")
    

api.add_resource(resource=Hotel_Indexer, key="/indexer")

# this to be able to run this api directly using python
if __name__ == "__main__":
    app.run(debug=True)
    

    