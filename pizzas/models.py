from django.db import models

##### тип пиццы, время готовки  размер стоимость
class types_pizza(models.Model):
    pizza_type = models.CharField(max_length= 30, help_text="type pizza")
    # цена по размерам 30 35 40 45
    price_small = models.BigIntegerField(help_text="price_small")
    price_midle = models.BigIntegerField(help_text="price_midle")
    price_large = models.BigIntegerField(help_text="price_large")
    price_very_large = models.BigIntegerField(help_text="price_very_large")
    def __str__(self):
        return  str(self.pizza_type) + "price: " + str(self.price_small) + "  "+ str(self.price_midle) + str(self.price_large ) + str(self.price_very_large)




### тип данных для заказа
class order_to_user(models.Model):
    id_oder = models.AutoField(primary_key =True, )
    adress_order = models.CharField(max_length=30)
    def __str__(self):
        return  self.adress_order



### тут хранится пицца заказанная и прекрепляется к заказу

class pizza(models.Model):
    SIZE_CHOISE=[
        ("sm", "small"),
        ("md", "middle"),
        ("lg", "large"),
        ("vlg", "very large" ),
    ]
    pizza_nomet = models.BigIntegerField()
    pizza_type = models.ForeignKey(types_pizza , on_delete=models.CASCADE)
    ### с размером как то решить надо
    pizza_size = models.CharField(max_length= 5, choices=SIZE_CHOISE, default="md", verbose_name="размер")
    order_pizza = models.ForeignKey(order_to_user, on_delete=models.CASCADE)
    number_of_units_pizza= models.BigIntegerField(  unique=False )
    price = models.BigIntegerField()
    def __str__(self):
        return  str(self.pizza_type) +"   "+str(self.number_of_units_pizza) + "шт"

##sdasdasdasd