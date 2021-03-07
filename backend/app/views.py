from django.http import HttpResponse
from .models import CouriersTest
from django.core.serializers import serialize



def sendjson(request):
    courier = CouriersTest.objects.all()
    data = serialize('json',courier,fields=('name','lat','lng'))
    return HttpResponse(data, content_type="application/json")

def sendsql(request):
    courier = CouriersTest.objects.all()
    riders_json = serialize('json', courier)
    return HttpResponse(riders_json,content_type="application/json")