from django.db import models
from django.db.models import CASCADE


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Types(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=110)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Book_list(models.Model):

    GENRE_TYPE = (
        ("Poem", "Poem"),
        ("Comedy", "Comedy"),
        ("Fantasy", "Fantasy"),
        ("Epos", "Epos"),
        ("Thriller", "Thriller"),
        ("Romance", "Romance"),
    )

    name = models.CharField(max_length=100, verbose_name="Название книги", null=True)
    image = models.ImageField(
        upload_to="book_images/", verbose_name="Загрузите обложку книги", null=True
    )
    about_book = models.TextField(verbose_name="О чем книга", null=True)
    genre_type = models.CharField(
        null=True, max_length=20, choices=GENRE_TYPE, verbose_name="Какой жанр"
    )
    date_of_creation = models.DateField(verbose_name="Дата создания книги", null=True)
    link_to_book = models.URLField(verbose_name="Прикрепите ссылку", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.genre_type}"

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class ReviewsBooks(models.Model):
    review_book = models.ForeignKey(
        Book_list, on_delete=CASCADE, related_name="reviews_books"
    )
    text = models.TextField()
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.points} - {self.review_book}"
