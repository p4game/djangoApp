from django.contrib.auth import authenticate,login,logout,get_user,get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
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

@login_required
def show_forecast(request):
    user = get_user(request)
    print(type(user.get_forecasts_by_type(1)))
    user_model = get_user_model()

    encodedjson = serializers.serialize("json", user.get_forecasts_by_type(1))
    #print(encodedjson)
    return HttpResponse(user.toJSON())

