from django.http import HttpResponse
from datetime import datetime

def test(equest):
    date = datetime.now()
    print("test function is called from view")
    return HttpResponse("<h1>Hello this is index page</h1>" + str(date)) 