from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200) # the size of topic text box
    #auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #creates 1 to M relationship entre topic and entry
    text = models.TextField() # create a textfield
    date_added = models.DateTimeField(auto_now_add=True) #date added field

    class Meta:
        #it allows us to set a special attribute telling Djanog to use "Entries"
        #when it needs to refer to >1 entry. W/out this, Django
        #would refer to multiple entries as "Entrys"
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return f"{self.text[:50]}..."

        