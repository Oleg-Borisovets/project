from django.db import models

# Create your models here.
# создаем табличку в которой будет 2 столбца первый имя автора второй описание 
class Author(models.Model):
    Author_neme = models.CharField("neme", max_length=50)
    Author_description = models.CharField("description", max_length=200)
    def __str__(self):
        return self.Author_neme