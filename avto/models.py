from django.db import models

# Create your models here.









class Avtosalon(models.Model):
    avto_nomi=models.CharField(max_length=255)
    image = models.ImageField(upload_to="news_images/")
    xaqida=models.TextField()
    narxi=models.IntegerField()
    qushimcha_malumot_nomi=models.TextField()

    def __str__(self):
        return self.avto_nomi


class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=250)
    matn = models.TextField()
    rasmlar = models.ImageField(upload_to='yangilik_rasmlar/')
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha