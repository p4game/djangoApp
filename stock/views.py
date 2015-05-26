from django.contrib.auth import authenticate,login,logout,get_user,get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def login_view(request):
    account = request.GET["account"]
    password = request.GET["password"]
    user = authenticate(account=account, password=password)
    if user is not None:
        login(request, user)
        user.get_forecasts_by_type(1)
        return HttpResponse("hello world")
    return HttpResponse("login failed")

def logout_view(request):
    logout(request)
    return HttpResponse("logout")

@login_required
def show_forecast(request):
    user = get_user(request)
    user_model = get_user_model()
    return HttpResponse("show_forecast")

