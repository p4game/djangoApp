from django.contrib.auth import authenticate,login,logout,get_user,get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from stock.forecast import ForecastController
def login_view(request):
    account = request.GET["account"]
    password = request.GET["password"]
    user = authenticate(account=account, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("hello world")
    return HttpResponse("login failed")

def logout_view(request):
    logout(request)
    return HttpResponse("logout")

forecast = ForecastController()
@login_required
def show_forecast(request):
    user = get_user(request)
    user_model = get_user_model()
    list = forecast.get_day_list()
    #print(json.dumps(list))
    #serializers.serialize("json", list)
    return HttpResponse(serializers.serialize("json", list))

