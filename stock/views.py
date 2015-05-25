from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
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

def getForecastByUser(request):

    return HttpResponse("getForecastByUser")

