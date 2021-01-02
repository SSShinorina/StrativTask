import coreapi
from rest_framework import viewsets
from django.http import HttpResponse
from assignment.task.models import Get_details, Details
from assignment.assignment.serializers import DetailSerializer


# def home(request):
#     response = requests.get('https://restcountries.eu/rest/v2/all')
#     data = response.json()
#     return render(request, 'core/home.html', {
#
#         'name': data['name'],
#         'alpha2code': data['alpha2code'],
#         'capital': data['capital'],
#         'population': data['population'],
#         'timezone': data['timezone'],
#         'flag': data['flag'],
#         'languages': data['languages'],
#         'borders': data['borders']
#
#     })


def home(request):
    client = coreapi.Client()
    data = client.get('https://restcountries.eu/rest/v2/all')

    name = data.get("name")
    alpha2code = data.get("alpha2code")
    capital = data.get("capital")
    population = data.get("population")
    timezone = data.get("timezone")
    flag = data.get("flag")
    languages = data.get("languages")
    borders = data.get("borders")

    details = Get_details.objects.create(name=name, alpha2code=alpha2code, capital=capital, population=population,
                                         timezone=timezone, flag=flag, languages=languages, borders=borders)
    details.save()

    return HttpResponse("Get and Save Details")


