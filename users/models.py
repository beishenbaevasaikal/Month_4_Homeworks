from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfileUser(User):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    phone_number = models.CharField(max_length=14, default='+996', null=True)
    age = models.PositiveIntegerField(default=18,
                                      validators=[
                                          MaxValueValidator(90),
                                          MinValueValidator(5)
                                      ], null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    club = models.CharField(max_length=20, null=True, default='Категория не определена')

@receiver(post_save, sender=ProfileUser)
def set_category(sender, instance, create, **kwargs):
    print('Сигнал успешен, пользователь зарегистрирован')
    age = instance.age
    if age <5:
        instance.club = 'Категория не присваивается'
    elif age >=5 and age <= 10:
        instance.club = "Первая категория"
    elif age >=11 and age <= 15:
        instance.club = "Вторая категория"
    elif age >=16 and age <=25:
        instance.club = "Высшая категория"
    else:
        instance.club = "Категория не определена"
    instance.save()