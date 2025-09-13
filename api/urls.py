from django.urls import path
from . import views 

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>',views.studentsDetailView),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeesDetail.as_view()),
]
