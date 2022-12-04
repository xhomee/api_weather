from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api()

api_key2 = "ffa6fb28ddc93a989990104dd6336e72"

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    city = args.get("city", default="Kyiv", type=str)
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key2}&units=metric"
    r = requests.get(link)
    weather = r.json()
    #api_weather = weather["main"]["temp"]
    #print(weather)
    if weather["cod"] == '404':
        return {'cod': '404', 'message': 'city not found'}
    else:
        api_weather = {"city": weather["name"], "temp": weather["main"]["temp"]}
        return api_weather


# class Main(Resource):
#     def get(self):
#         return api_weather

# class Main(Resource):
#     def get(self, city_id):
#         if city_id == 0:
#             return {"empty": 0}
#         else:
#             return city_api_id[city_id]
#         #return api_weather
#         #return {"temp": weather["main"]["temp"], "city": city}


# api.add_resource(Main, "/api")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

