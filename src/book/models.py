from django.db import models

# Create your models here.
# создаем табличку в которой будет 2 столбца первый имя автора второй описание 
class Author(models.Model):
    Author_name = models.CharField(
        verbose_name="name", 
        max_length=50)
    Author_description = models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
    def __str__(self):
        return self.Author_name
# добовляем табличку с серия книг 2 поля первая какая серия книги  вторая описание серии .
class Series(models.Model):
    series = models.CharField(
        verbose_name="Series",
        max_length=20, 
        blank=True,
        null=True)
    series_description=models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
    def __str__(self):
        return self.series


#Добовляем табличку жанр 

class Genres(models.Model):
    genres =models.CharField(
        verbose_name="genres",
        max_length=20, 
        blank=True,
        null=True)
    genres_description=models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
    def __str__(self):
        return self.genres        

# Добавить издатесьство 

class Publisher(models.Model):
    publisher =models.CharField(
        verbose_name="publisher",
        max_length=50, 
        blank=True,
        null=True)
    publisher_description=models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
    def __str__(self):
        return self.publisher 