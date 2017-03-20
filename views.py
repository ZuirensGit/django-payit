from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from rest_framework.renderers import JSONRenderer

from .models import Spgateway
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    return JSONResponse({'ec': -1})


import random
class PayApiView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                merchant_id = request.POST.get('merchant_id')
                if merchant_id:
                    merchant = Spgateway.objects.get(merchant_id=merchant_id)
                    status = self._fire(merchant)
                    merchant.status = status
                    merchant.save()
                    return JSONResponse({'ret': 0, 'api_status': status})
                else:
                    return JSONResponse({'ret': 1})
            except Exception as e:
                print(e)
                return JSONResponse({'ret': -1})

        return JSONResponse({'ret': 99})

    def _fire(self, merchant):
        status = ['success', 'error'][random.randint(0, 1)]

        return status