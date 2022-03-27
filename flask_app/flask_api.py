from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


hotel_arg = reqparse.RequestParser()
hotel_arg.add_argument(hotel, type=str, help="Please select the hotel", required=True)

    
class Hotel_Tone_Analyzer(Resource):
    """the tone analyzer class"""

    def get(self, hotel):    
        hotel = hotel_arg.parse_args()
        print("<h1>the total emotional tones for a hotel</h1>")
        return {hotel: hotel_arg}
    

class Hotel_Indexer(Resource)
    """the hotel indexer class"""

    def get(self):
        return "<p>Hello, World! hotel_indexer</p>"


api.add_resource(resource=Hotel_Tone_Analyzer, key="/toneanalyzer/<string:hotel>")
api.add_resource(resource=Hotel_Indexer, key="/indexer")

# this to be able to run this api directly using python
if __name__ == "__main__":
    app.run(debug=True)
    
