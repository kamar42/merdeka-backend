from django.contrib import admin
from .models import BaseUnit, Commodities, Data, Goods, GoodsChilds, Province, City, TypeVenue, Venues

admin.site.register(BaseUnit)
admin.site.register(Commodities)
admin.site.register(Data)
admin.site.register(Goods)
admin.site.register(GoodsChilds)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(TypeVenue)
admin.site.register(Venues)
