from django.shortcuts import render_to_response
from models import Entry
def index(request):
    return render_to_response('blog/list.html', 
                              {'entries':
                                Entry.objects.all().order_by("publish_date").reverse()[:5]})

