from django.contrib import admin

from .models import MenuItem, Orders, Ingredient, IngredientInclusion, WaiterCall, PaymentAuthorization
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Orders)
admin.site.register(Ingredient)
admin.site.register(IngredientInclusion)
admin.site.register(WaiterCall)
admin.site.register(PaymentAuthorization)