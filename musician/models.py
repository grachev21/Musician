from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    title = models.CharField(max_length=100)


class Profession(models.Model):
    title = models.CharField(max_length=1000)


class Experience(models.Model):
    EXP = (
        ('a', 'Начинающий - от 0 до 1 год.'),
        ('b', 'Средний - от 1 года до 3 лет.'),
        ('c', 'Профессионал - от 10 лет и выше.')
    )
    experience = models.CharField(max_length=100, choices=EXP, default='a')


class Genre(models.Model):
    genre_style = models.CharField(max_length=100)

# ******************************************************************************


class Announcement(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    performance_experience = models.BooleanField()


class ProfileUser(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='archives/', null=True, blank=True)
    performance_experience = models.BooleanField()
    about = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    video = models.FileField(upload_to='archives/', null=True, blank=True)
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
