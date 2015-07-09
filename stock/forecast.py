from stock.models import Forecast, User
class ForecastController:
    list = []
    def __init__(self):
        print("ForecastController init")

    def get_day_list(self):
        print(len(self.list))
        if len(self.list) == 0 :
            print("aaaaaaaa")
            self.list = Forecast.objects.filter(type=1)

        #self.list = [1,2,2,3]

        return self.list




