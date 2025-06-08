from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.

# Whats shown on the menu, and whats included in Order objects
class MenuItem(models.Model):
    categoryOptions = {  
        ('starters', 'Starter'),
        ('mains', 'Main'),
        ('desserts', 'Dessert'),
        ('drinks', 'Drink')
    } 

    spiceOptions = {  
        ('spiceless', 'Spiceless'), #there is no filter option for this but it is the default option (?)
        ('mild', 'Mild'),
        ('hot', 'Hot'),
        ('atomic', 'Atomic')
    }   

    allergyOptions = {
        ('none', 'None'), #there is no filter option for this but it is the default option (?)
        ('dairy', 'Dairy'),
        ('gluten', 'Gluten'),
        ('nuts', 'Nuts'),
        ('vegetarian', 'Vegetarian')
    } 


    menuItemID = models.AutoField(primary_key=True)
    available = models.BooleanField()

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120, default = 'Delicious meal')
    price = models.FloatField()
    calories = models.IntegerField(validators=[MaxValueValidator(3500)], default = 150)
    image = models.ImageField(upload_to='MenuItemImages/', blank=False, null=False)
    category = models.CharField(max_length=30, default = 'mains', choices=categoryOptions)
    spice = models.CharField(max_length = 15, default = 'spiceless', choices=spiceOptions)
    allergy = models.CharField(max_length = 30, default = 'none', choices=allergyOptions) #uses string, not discrete options

    def __str__(self):
        return self.name
    
    def getAvailable():
        return MenuItem.objects.filter(available=True)
    
    def getNotAvailable():
        return MenuItem.objects.filter(available=False)

class Orders(models.Model):
    statusOptions = {
        ("REC", "Received"),
        ("CKG", "Cooking"),
        ("RTC", "Ready to collect"),
        ("UPD", "Not paid for"),
        ("COM", "Completed"),
    }
    orderID = models.AutoField(primary_key=True)
    table = models.IntegerField()
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE) 
    quantity = models.IntegerField()
    status = models.CharField(max_length=3, choices=statusOptions) #default="REC"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.menuItem) + " - " + str(self.quantity) + " to table no. " + str(self.table)
    
    class Meta:
        ordering = ['timestamp']

#06.02.24
#Ingredients
class Ingredient(models.Model):
    ingredientID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

#08.02.24
#Can define what ingredients a certain menu item contains
class IngredientInclusion(models.Model):
    dish = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.ingredient) + " in " + str(self.dish))


#13.02.24
# Messages visible to waiters from kitchen or customer.
class WaiterCall(models.Model):

    originOptions = {
        "CUS": "Customer",
        "KIT": "Kitchen"
    }
    origin = models.CharField(max_length=3,
                choices=originOptions.items(),
                default="CUS")

    waiterCallID = models.AutoField(primary_key=True)
    table = models.IntegerField()
    message = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "Table " + str(self.table) + ": " + str(self.message)
    
    #https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/
    def isStale(self):
        return timezone.now() > self.timestamp + timezone.timedelta(hours=12)
        #true IFF order is too old.

    #https://docs.djangoproject.com/en/5.0/ref/models/options/
    class Meta:
        ordering = ['timestamp']


#Currently not imported into admin.py
class PaymentAuthorization(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)
    payment_method = models.CharField(max_length=20)
    table_number = models.IntegerField()
    total_cost = models.FloatField(null=True, blank=True) 

    def authorize_payment(self):
        return True
        #can use API or checksum later
    
    def calculate_payment_cost(self):
        total_cost = 0

        orders = Orders.objects.filter(table=self.table_number)

        for order in orders:
            menu_item = order.menuItem
            order_cost = menu_item.price * order.quantity

            total_cost += order_cost

        return round(total_cost,2)    

    def save(self, *args, **kwargs):
        if not self.pk and self.total_cost is None:
            self.total_cost = self.calculate_payment_cost()

        super().save(*args, **kwargs)

    def __str__(self):
        return "Payment-Table: " + str(self.table_number) + " - £" + str(self.total_cost)
    