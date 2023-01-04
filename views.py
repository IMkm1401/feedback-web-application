from django.shortcuts import render,reditect
from . import forms,models
def feedback(request):
    form = forms.form_name()
    if request.method == "POST":
        form = forms.form_name(request.POST)
        if form.is_valid():
              form.save()
   form = forms.form_name()
   return render(request,"feedbacks.html",{"feedbackform":form})
  
