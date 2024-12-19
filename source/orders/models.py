from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5,blank=False, null=False)
    robot_model = models.CharField(max_length=2, default='default_model')
    robot_version = models.CharField(max_length=2, default='default_version')
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Заказ на {self.robot_model} v{self.robot_version} от {self.customer.email}"
