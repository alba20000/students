from django.urls import path
from core import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('group/<int:group_id>/', views.Group.as_view(), name='group'),
    path('discipline/<int:discipline_id>/', views.Discipline.as_view(), name='discipline'),
    path('student/<int:student_id>/', views.Student.as_view(), name='student')
]
