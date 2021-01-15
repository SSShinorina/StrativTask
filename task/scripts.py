import requests
from django.http import HttpResponse
from rest_framework.schemas import coreapi

from task.models import GetData

result = requests.get("https://restcountries.eu/rest/v2/all")
name = requests.get("https://restcountries.eu/rest/v2/all?fields=name")
alpha2code = requests.get("https://restcountries.eu/rest/v2/all?fields=alpha2code")
capital = requests.get("https://restcountries.eu/rest/v2/all?fields=capital")
# population = requests.get("https://restcountries.eu/rest/v2/all?fields=population")
# timezone = requests.get("https://restcountries.eu/rest/v2/all?fields=timezone")
# flag = requests.get("https://restcountries.eu/rest/v2/all?fields=flag")
# languages = requests.get("https://restcountries.eu/rest/v2/all?fields=languages")
# borders = requests.get("https://restcountries.eu/rest/v2/all?fields=borders")
#
details = GetData.objects.create(name=name, alpha2code=alpha2code, capital=capital)

#
#
#
#
# def home(request):
#     client = coreapi.Client()
#     data = client.get('https://restcountries.eu/rest/v2/all')
