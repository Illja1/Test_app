from django.db import models



class CSVData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return  self.name

