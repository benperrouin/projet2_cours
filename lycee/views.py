from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm, PresenceForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  listestud = Student.objects.filter(cursus=cursus_id)
  cursusresult = get_object_or_404(Cursus, pk=cursus_id)
  res= {'listestud': listestud, 'cursus': cursusresult
  }
  return render (request, 'lycee/student/infostud.html' , res)

def detail_col(request, cursus_id):
    chktud = Student.objects.filter(cursus=cursus_id)
    cursusresult = get_object_or_404(Cursus, pk=cursus_id)
    res2= {'chkstud': chkstud, 'cursus': cursusresult
  }
  #return render (request, 'lycee/student/callofroll.html' , res2)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentModif(UpdateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/edit.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))


class Particular_COL(CreateView):
  # ref au modEle
  model = Presence
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/student/part_col.html"
    # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))





  
    
