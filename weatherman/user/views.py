import requests
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required


from .models import Users

city = "Moscow, RU"
appid = settings.OPENWEATHERMAP_API_TOKEN


def show_main(request):
    print("Test test test")

    res = requests.get("http://api.openweathermap.org/data/2.5/find",
            params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    print(data)
    current_temperature = data['list'][0]['main']['temp']
    print()
    print(f"Current temperature in Moscow: {current_temperature}")


    context = {}
    context['temperature_moscow'] = current_temperature

    return render(request, "index.html", context)


@login_required
def profile_view(request):
    return render(request, "profile.html")
