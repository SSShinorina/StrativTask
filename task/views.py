import coreapi
from django.http import HttpResponse
from rest_framework import viewsets, filters
from task.models import Details, Language, Border

from assignment.serializers import LanguageSerializer, BorderSerializer, DetailsSerializer


class Get_details(object):
    pass


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


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class BorderViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


# class SpeakViewSet(viewsets.ModelViewSet):
#     queryset = Speak_language.objects.filter(name='Bangla')
#     serializer_class = SpeakSerializer

#
# @api_view(['PUT', 'DELETE'])
# def border(request, pk):
#     try:
#         queryset = Border.objects.get(pk=pk)
#     except Border.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = BorderSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         border.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# class BorderAPIViewTest(ListCreateAPIView):
#     """
#     API view to retrieve list of posts or create new
#     """
#     serializer_class = BorderSerializer
#     queryset = Border.objects.active()
#
#
# class BorderAPIViewTest(RetrieveUpdateDestroyAPIView):
#     """
#     API view to retrieve, update or delete post
#     """
#     serializer_class = BorderSerializer
#     queryset = Border.objects.all()
