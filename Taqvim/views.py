from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .payer import pray_time

@api_view(['GET'])
def home(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    shaxar = body['shaxar']
    til = body['til']
    res = pray_time(shaxar, til)
    resp = Response()
    resp.data = res

    return resp

