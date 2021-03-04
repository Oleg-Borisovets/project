from django.db import models

# Create your models here.
# создаем табличку в которой будет 2 столбца первый имя автора второй описание 
class Author(models.Model):
    author_name = models.CharField(
        verbose_name="name", 
        max_length=50)
        # Для того что бы сделать фото 
    # pic = models.ImageField(
    #     verbose_name='Picture',
    #     upload_to = 'uploads/')    
    author_description = models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
    def __str__(self):
        return self.author_name
# добовляем табличку с серия книг 2 поля первая какая серия книги  вторая описание серии .
class Series(models.Model):
    series = models.CharField(
        verbose_name="Series",
        max_length=50)
    
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
# class Book(models.Model):
# # Название книги +  
# Фото обложки  
# Цена (BYN) +
# Авторы книги (может содержать несколько авторов) - справочни +
# Серия - справочник +
# Жанры (один или несколько жанров) - справочник +
# Год издания +
# Страниц +
# Переплет +
# Формат +
# ISBN +
# Вес (гр) +
# Возрастные ограничения +
# Издательство - справочник +
# Количество книг в наличии + 
# Активный (доступен для заказа, Да/Нет)+
# Рейтинг (0 - 10) +
# Дата внесения в каталог +
# Дата последнего изменения карточки +

class Book(models.Model):
    # Название книги
    name = models.CharField(
        verbose_name="name",
        max_length=20  
    )         

    # Фото обложки  
    pic = models.ImageField(
        verbose_name='Picture',
        upload_to = 'uploads/') 
        
    # Цена (BYN)
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=5,
        decimal_places=2)
    # Переплет
    binding =models.CharField(
        verbose_name="binding",
        max_length=20
        )

    # Формат
    
    format = models.CharField(
        verbose_name="format",
        max_length=10
        )

    # isbn 
    isbn = models.PositiveSmallIntegerField(
        verbose_name="ISBN")       
        
    # Страниц
    pages = models.PositiveSmallIntegerField(
        verbose_name="pages")   
    # Вес (гр) 
    the_weight = models.PositiveSmallIntegerField(
        verbose_name="the weight")    
    
    # Возрастные ограничения    
    age_restrictions = models.PositiveSmallIntegerField(
        verbose_name="age restrictions")

    # Количество книг в наличии    
    amount = models.PositiveSmallIntegerField(
        verbose_name="amount ")

    # Рейтинг
    
    rating = models.PositiveSmallIntegerField(
        verbose_name="rating")
        
    # Авторы книги (может содержать несколько авторов) - справочни
    author = models.ForeignKey(
        'book.Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name='Author1'
    )

    # Серия - справочник
    
    series = models.ForeignKey(
        'book.Series',
        verbose_name='Series',
        on_delete=models.PROTECT,
        related_name='Series1'
    )

    # Жанры (один или несколько жанров) - справочник
    genres = models.ForeignKey(
        'book.Genres',
        verbose_name='Genres',
        on_delete=models.PROTECT,
        related_name='Genres1'
    )

    # Издательство - справочник
    publisher = models.ForeignKey(
        'book.Publisher',
        verbose_name='Publisher',
        on_delete=models.PROTECT,
        related_name='Publisher1'
    )
    # Дата внесения в каталог
    created = models.DateTimeField(
        verbose_name='Created',
        auto_now=False, # время изменения 
        auto_now_add=True # время добовление 
    )
    # Дата последнего изменения карточки

    update = models.DateTimeField(
        verbose_name='Update',
        auto_now=True,
        auto_now_add=False
    )

  
    # Год издания 
    
    year_edition = models.DateField(
        verbose_name="Year Edition"
    )

    # Активный (доступен для заказа, Да/Нет)
    active = models.BooleanField(
        verbose_name="Active")



class Home(models.Model):
    pass
    # Название книги
    # name = models.CharField(
    #     verbose_name="name",
    #     max_length=20  
    # )
    # author_name = models.CharField(
    #     verbose_name="name", 
    #     max_length=50)       