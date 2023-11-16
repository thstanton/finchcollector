from django.db import models
from django.urls import reverse

PLACES = (
    ('F', 'Front Garden'),
    ('B', 'Back Garden'),
    ('A', 'Allotment'),
)

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    appearance = models.TextField(max_length=250)
    seen = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})

class Sighting(models.Model):
    date = models.DateField('date seen')
    location = models.CharField(
        max_length=1,
        choices = PLACES,
        default=PLACES[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
