import requests
import json

api_key2 = "ffa6fb28ddc93a989990104dd6336e72"
#print("Привіт тут буде прогноз погоди")
#city = input("Введіть місто для показу температури: ")
city = "kyiv"

link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key2}&units=metric"
#test_json = json.loads(json.text)

r = requests.post(link)

weather = r.json()

#print(r.headers)

print(r.status_code)


print(weather["main"]["temp"])
print(weather["name"])

print(r.url)

#print(req.content)




#localhost:5000/api/weather?sity=kyiv&hyi=15




#
# const query = req.body.cityName;
#   const apiKey = "ffa6fb28ddc93a989990104dd6336e72"
#   const unit = "metric"
#   const url = "https://api.openweathermap.org/data/2.5/weather?q=" + sity + "&appid=" + apiKey + "&units=" + unit;