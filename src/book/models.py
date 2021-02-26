from django.db import models

# Create your models here.
# создаем табличку в которой будет 2 столбца первый имя автора второй описание 
class Author(models.Model):
    Author_name = models.CharField(
        verbose_name="name", 
        max_length=50)
        # Для того что бы сделать фото 
    # pic = models.ImageField(
    #     verbose_name='Picture',
    #     upload_to = 'uploads/')    
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


# карточка товара 
class Book(models.Model):
# Название книги
    name = models.CharField(
        verbose_name="name", 
        max_length=50)     
# Фото обложки  
    # pic = models.ImageField(
    #     verbose_name='Picture',
    #     upload_to = 'uploads/')
# Цена (BYN)
    Price = models.PositiveSmallIntegerField(
        verbose_name="Price")
# Авторы книги (может содержать несколько авторов) - справочни
    Author = models.ForeignKey(
        'book.Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name='Author1'
    )
# Серия - справочник
# Жанры (один или несколько жанров) - справочник
# Год издания
# Страниц
# Переплет
# Формат
# ISBN
# Вес (гр)
# Возрастные ограничения
# Издательство - справочник
# Количество книг в наличии
# Активный (доступен для заказа, Да/Нет)
# Рейтинг (0 - 10)
# Дата внесения в каталог
# Дата последнего изменения карточки

