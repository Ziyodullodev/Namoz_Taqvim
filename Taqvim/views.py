from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .payer import pray_time

@api_view(['GET'])
def UzTaqvim(request, pk):
    res = pray_time(pk, "uz")
    resp = Response()
    resp.data = res
    return resp

@api_view(['GET'])
def KrTaqvim(request, pk):
    res = pray_time(pk, "kr")
    resp = Response()
    resp.data = res
    return resp


@api_view(['GET'])
def RuTaqvim(request, pk):
    res = pray_time(pk, "kr")
    resp = Response()
    resp.data = res
    return resp


def About(request):
    return render(request, 'index.html')

