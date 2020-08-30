from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentModif, Particular_COL

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^student/edit/(?P<pk>\d+)$', StudentModif.as_view(), name='modifstudent'),
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/part_col/$', Particular_COL.as_view(), name='part_col'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail_col'),
]