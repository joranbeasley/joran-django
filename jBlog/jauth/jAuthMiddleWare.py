__author__ = 'Joran'
from django.http import HttpResponse
class jAuthMiddleware:
    def process_request(self,request):
        x= HttpResponse(str(request.META['PATH_INFO']))