from django.db import models
from django.db.models import Count, F, Value
#from .models import Events
# Modeller burada tanimlanacak.





class Sessions (models.Model):



    session_name = models.CharField(max_length=10)
    session_start = models.FloatField()
    session_end = models.FloatField()
    speaker = models.CharField(max_length=10)





    def __str__(self):
        return self.session_name

class Events (models.Model):
    event_name = models.CharField(max_length=10)
    start_date = models.FloatField()
    end_date = models.FloatField()
    timezone = models.CharField(max_length=10)
    session_number=models.IntegerField(blank=True, null=True)

    events=models.ForeignKey(to=Sessions,on_delete=models.CASCADE)




    def __str__(self):
        return self.event_name
