from django.contrib import admin
from . import models

admin.site.register(models.Book_list)
admin.site.register(models.ReviewsBooks)
admin.site.register(models.Tag)
admin.site.register(models.Types)