from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from.models import Tender

class RegistrationForm(forms.ModelForm):
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={"placeholder": "Enter password"})
    )
  confirm_passowrd = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"})
    )

  class Meta:
    model = User
    fields = ["username", "email", "password"]


  def clean(self):
    cleaned = super().clean()
    p1 = cleaned.get("password")
    p2 = cleaned.get("confirm_password")
    if p1 != p2:
      raise forms.ValidationError("Passwords do not match.")
    return cleaned
  
class TenderForm(forms.ModelForm):
   class Meta:
      model = Tender
      fields = [
         "reference_no",
         "title",
         "description",
         "category",
         "opening_date",
         "closing_date",
         "status",
      ]  

      widgets = {
        "opening_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        "closing_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "reference_no": forms.TextInput(attrs={"class": "form-control"}),
        "category": forms.Select(attrs={"class": "form-select"}),
        "status": forms.Select(attrs={"class": "form-select"}),
      }