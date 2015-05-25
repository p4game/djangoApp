from stock.models import Forecast, User
class ForecastController:
    def get_list_by_user(account):
        user = User.objects.get(account=account)

