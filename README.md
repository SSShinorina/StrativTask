# StrativTask
This is a test
asgiref==3.3.1
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
click-default-group==1.2.2
coreapi==2.3.3
coreschema==0.0.4
Django==3.1.4
djangorestframework==3.12.2
idna==2.10
include==0.2.2
itypes==1.2.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Pillow==8.0.1
python-dateutil==2.8.1
pytz==2020.5
requests==2.25.1
six==1.15.0
sqlparse==0.4.1
tabulate==0.8.7
task==0.2.0
uritemplate==3.0.1
urllib3==1.26.2
django-tables2=2.3.3

Need to install these packages. 
 
Run Script: open python shell by "python manage.py shell" and write 
            1.from task.scripts import *
            2.resut.status_code
            3.result.text
            4.result.json()
            
To view data fetches from api: 
            1. python manage.py runserver
            2."data": "http://127.0.0.1:8000/data/"
API Views:
            1. list of all countries-- http://127.0.0.1:8000/border/,
            2. details of country api -- http://127.0.0.1:8000/detail/,
            3. language api --- http://127.0.0.1:8000/language/

Information of country : http://127.0.0.1:8000/country/
For search country : http://127.0.0.1:8000/country/ (search field)
For getting details of specific country : http://127.0.0.1:8000/search/ (click details button)


Run using command python manage.py runserver. 
1. For login you need to use \login after the provided  ip address. I created superuser using command line. username : "lenovo" and password : 123
2. To view the templates you need to use \countries where the desired table exist and search filed.
