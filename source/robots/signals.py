from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Robot
from orders.models import Order

@receiver(post_save, sender=Robot)
def robot_availability_changed(sender, instance, **kwargs):
    if instance.is_available:
        orders = Order.objects.filter(
            robot_model=instance.model,
            robot_version=instance.version,
            is_notified=False
        )
        for order in orders:
            send_mail(
                subject='Робот в наличии!',
                message=f'Добрый день!\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами',
                from_email='bzmelisv@gmail.com',
                recipient_list=[order.customer.email],
                fail_silently=False,
            )
            order.is_notified = True
            order.save()