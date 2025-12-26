from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):
    time_choice = (
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
    )
    GUESTS_CHOICES = (
        ('1 personne', '1 personne'),
        ('2 personne', '2 personne'),
        ('3 personne', '3 personne'),
        ('4 personne', '4 personne'),
        ('5 personne', '5 personne'),
        ('6 personne', '6 personne'),
        ('8+ personne', '8+ personne'),
    )
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=250, choices=time_choice)
    number_of_guests = models.CharField(max_length=250, choices=GUESTS_CHOICES)

    def __str__(self):
        return f"{self.full_name} reserved a table for {self.number_of_guests} at {self.time} on {self.date}"
