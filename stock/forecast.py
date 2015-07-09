from stock.models import Forecast, User
class ForecastController:
    list = None
    def __init__(self):
        print("ForecastController init")

    def get_day_list(self):
        if self.list == None :
            self.list = []
            forecasts = Forecast.objects.filter(type=1)
            for k in forecasts:
                print(k)

        #self.list = [1,2,2,3]

        return self.list




