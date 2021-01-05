from django_tables2 import tables

from task.models import Details


class CountryTable(tables.Table):
    class Meta:
        model = Details
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "alpha2code", "capital", "population", "timezone", "flag")


class DetailsTable(tables.Table):
    class Meta:
        model = Details
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "borders", "languages")
