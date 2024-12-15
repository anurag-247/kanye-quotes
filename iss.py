import requests
import datetime
import smtplib

MY_LAT = 26.202601
MY_LONG = 78.184192

MY_EMAIL = 'captainrogers3069@gmail.com'
MY_PASSWORD = '**********'

my_time = datetime.datetime.now().time().hour
# print(my_time)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

iss = requests.get("http://api.open-notify.org/iss-now.json")
iss.raise_for_status()
iss_data = iss.json()
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])
# print(iss_lat)
# print(iss_lng)

if my_time > sunset:
    if my_time < sunrise:
        if (int(iss_lat) in range(int(MY_LAT) - 5, int(MY_LAT) + 5)
                and int(iss_lng) in range(int(MY_LONG) - 5, int(MY_LONG) + 5)):
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="tonystark3069@yahoo.com",
                                msg="Subject:Look up\n\nISS is above you")
            print("email sent")
