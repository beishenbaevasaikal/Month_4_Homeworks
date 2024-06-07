from django.db import models

# Create your models here.
class Book_list(models.Model):

    objects = None
    GENRE_TYPE = (
        ('Poem', 'Poem'),
        ('Comedy', 'Comedy'),
        ('Fantasy', 'Fantasy'),
        ('Epos', 'Epos'),
        ('Thriller', 'Thriller'),
        ('Romance', 'Romance'),
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    about_book = models.TextField()
    genre_type = models.CharField(null=True, max_length=20, choices=GENRE_TYPE)
    date_of_creation = models.DateField()
    link_to_book = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.genre_type}'
    
    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
