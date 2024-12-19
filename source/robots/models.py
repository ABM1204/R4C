from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False, default='default_model')
    model = models.CharField(max_length=2, blank=False, null=False, default='default_model')
    version = models.CharField(max_length=2, blank=False, null=False, default='default_version')
    created = models.DateTimeField(blank=False, null=False, default=datetime.now)

    def save(self, *args, **kwargs):
        validate_robot_data({
            "serial": self.serial,
            "model": self.model,
            "version": self.version,
            "created": self.created.strftime("%Y-%m-%d %H:%M:%S"),
        })
        super().save(*args, **kwargs)


def validate_robot_data(data):
    required_fields = ["serial", "model", "version", "created"]

    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Пропущено поле: {field}")

    if len(data.get("serial", "")) >= 5:
        raise ValidationError("Максимальная длинна 'serial': 5.")

    if len(data.get("model", "")) >= 2:
        raise ValidationError("Максимальная длинна 'model': 2.")

    if len(data.get("version", "")) >= 2:
        raise ValidationError("Максимальная длинна 'version': 2.")

    try:
        datetime.strptime(data["created"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValidationError("Неверный формат даты. Используйте 'YYYY-MM-DD HH:MM:SS'.")

    if datetime.strptime(data["created"], "%Y-%m-%d %H:%M:%S") > datetime.now():
        raise ValidationError("Поле 'created' не может быть в будущем времени.")



class RobotProduction(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    produced_at = models.DateTimeField()

    def __str__(self):
        return f"{self.robot.model} {self.robot.version} - {self.quantity} шт."