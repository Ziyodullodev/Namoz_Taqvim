from django.shortcuts import render
import json
from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from django.http import JsonResponse


 
def Vaqtol(viloyat):
    # url = f"https://namozvaqti.uz/shahar/{viloyat}"
    url = "http://ziyodullo2000.myxost.uz/Taqvim/API/Api.php?city=fargona"
    headers = {
        "Accept-Language" : "en-US,en;q=0.5",
        "User-Agent": "Defined",
    }
    get_responce = requests.get(url, headers=headers)
    viloyat = get_responce.text
    # ok = viloyat.split('Hozirgi vaqt:')
    # asr1 = ok[1].split('<p class="time" id="asr">')
    # shom1 = asr1[1].split('const times = [')
    # shom = shom1[1].split('];')
    # shom = shom[0].replace('\n        ', '')
    # shom = shom.replace("'", '')
    # vaqt = shom.split(',')
    return viloyat


def home(request):
    vaqt = Vaqtol('margilon')
    # vaqt = vaqt.split(',')
    content = {
        'bomdod': vaqt,
        'quyosh': "vaqt[1]",
        'peshin': "vaqt[2]",
        'asr': "vaqt[3]",
        'shom': "vaqt[4]",
        'xufton':" vaqt[5]"

    }
    return render(request, 'index.html', content)


# class NamozApiView(APIView):
def Namoz_view(request, *args , **kwargs):

    if request.method == 'POST':
        data = {
            'ok':"True"
        }
        return JsonResponse(data)
    body = request.body
    try:
        data = json.loads(body)
    except:
        pass
    
    viloyat = Vaqtol(data['viloyat'])
    return_data = {
        "taqvim":{
            'bomdod': viloyat[0],
            'quyosh': viloyat[1],
            'peshin': viloyat[2],
            'asr': viloyat[3],
            'shom': viloyat[4],
            'xufton': viloyat[5],
            'manba':'https://namozvaqti.uz/'
        }
    }
    return JsonResponse(return_data)