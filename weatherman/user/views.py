from django.shortcuts import render
from django.conf import settings

from .models import Users


def show_main(request):
    context = {}
    print(f"API token: {settings.OPENWEATHERMAP_API_TOKEN}")

    return render(request, "index.html", context)
