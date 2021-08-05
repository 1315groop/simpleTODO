from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self):
        if self.died:
            return "{}, {} ({}-{})".format(
                self.last_name, self.first_name, self.born, self.died
            )
        return "{}, {} ({})".format(self.last_name, self.first_name, self.born)
