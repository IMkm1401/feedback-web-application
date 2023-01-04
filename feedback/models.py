from django.db import models
class model_name():
  # enter your fields 
  name = models.CharField(max-length=100)
  family = models.CharField(max-length=100)
  feedback = models.TextField()
  def __str__(self):
    return self.name +" "+self.family
  
    
