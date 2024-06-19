from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    data = {'val' : 3,'name':'josef','test' : 'String with spaces','datetime':datetime.datetime.now(),'py':'Python is fun','info':
        [
        {'name': 'Josh', 'age': 19},
        {'name': 'Dave', 'age': 22},
        {'name': 'Joe', 'age': 31},
        ],
        'fruits':['Apple', 'Mango', 'Orange'],
        }
    return render(request,'first_app/home.html',data)