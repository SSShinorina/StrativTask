import coreapi
from django.db.models import Q
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.generic import ListView
from django_tables2 import SingleTableView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from task.table import CountryTable, DetailsTable
from rest_framework import viewsets, filters, status
from task.models import CountryDetails, Language, Border, GetData
from assignment.serializers import LanguageSerializer, BorderSerializer, DetailsSerializer, LoginSerializer


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            usr = serializer.validated_data['user']
            tok, created = Token.objects.get_or_create(user=usr)
            return Response({'token': tok.key}, status=status.HTTP_200_OK)


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

    details = GetData.objects.create(name=name, alpha2code=alpha2code, capital=capital, population=population,
                                     timezone=timezone, flag=flag, languages=languages, borders=borders)
    details.save()

    return HttpResponse("Get and Save Details")


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class BorderViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = CountryDetails.objects.all()
    serializer_class = DetailsSerializer


class CountryListView(SingleTableView):
    model = CountryDetails
    table_class = CountryTable
    template_name = 'country.html'


class CountryDetailsView(SingleTableView):
    model = CountryDetails
    table_class = DetailsTable
    template_name = 'details.html'


class SearchResultsView(ListView):
    model = Border
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Border.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
