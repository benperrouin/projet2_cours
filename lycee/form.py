from django.forms.models import ModelForm
from .models import Student, Presence #Appel

class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
    fields  = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )

class PresenceForm(ModelForm):

  class Meta:
    model = Presence

    fields = (
      "reason",
      "isMissing",
      "Date",
      "student",
    )


#class AppelForm(ModelForm):

 # class Meta:
  #  model = Appel

   # fields = (
    #  "Date",
     #"checklist",
    #)