from django.shortcuts import render

from .models import Users


def show_main(request):
    context = {}

    return render(request, "index.html", context)
