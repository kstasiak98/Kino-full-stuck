from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=140)
    time_spend = models.IntegerField()
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    description = models.TextField()

    def __str__(self):
        return self.title


class Sall(models.Model):
    number_of_columns = models.IntegerField()
    number_of_rows = models.IntegerField()


class Seans(models.Model):
    seans_film = models.ForeignKey(Film,
                                   on_delete=models.CASCADE)
    seans_sall = models.ForeignKey(Sall, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Ticket(models.Model):
    seans_name = models.ForeignKey(Seans,
                                   on_delete=models.CASCADE)
    client = models.CharField(max_length=240)
    row = models.CharField(max_length=2)
    column = models.IntegerField()





