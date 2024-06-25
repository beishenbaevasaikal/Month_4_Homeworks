from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = models.ProfileUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'gender'
        )

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.ProfileUser)
def set_club(sender, instance, create, **kwargs):
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




