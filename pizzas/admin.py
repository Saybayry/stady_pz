from django.contrib import admin
from .models import types_pizza, pizza,order_to_user

admin.site.register(types_pizza)
admin.site.register(pizza)
admin.site.register(order_to_user)


# Register your models here.
