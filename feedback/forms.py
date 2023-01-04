from django import fomrs
from . import models
class form_name(forms.modelform):
  class Meta():
    model = models.,model_name
    fields = ["name","family","feedback"]
