from django.db import models
from django.utils import timezone
import hashlib


class User(models.Model):
    account = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account

    def hashed_password(self, password=None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password.encode()).hexdigest()

    def is_authenticated(self):
        return True

    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        else:
            return False

    def get_forecasts_by_type(self, type):
        list = self.forecast_set.filter(type = type)
        len = list.count()
        for i in range(0, len):
            forecast = list[i]
            print(forecast.type, forecast.value,timezone.localtime(forecast.last_forecast))
        print(list)

class Forecast(models.Model):
    type = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(User)
    last_forecast = models.DateTimeField(default=timezone.now)
