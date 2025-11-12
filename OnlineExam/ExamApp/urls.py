from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('AdminLogin.html', views.AdminLogin, name="AdminLogin"), 
	       path('StudentLogin.html', views.StudentLogin, name="StudentLogin"), 
	       path('Register.html', views.Register, name="Register"),
	       path('Signup', views.Signup, name="Signup"),
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('StudentLoginAction', views.StudentLoginAction, name="StudentLoginAction"),
	       path('ViewStudents', views.ViewStudents, name="ViewStudents"),
	       path('ViewGrades', views.ViewGrades, name="ViewGrades"),
	       path('WriteExam', views.WriteExam, name="WriteExam"),
	       path('CheckGrade', views.CheckGrade, name="CheckGrade"),
	       path('WriteExamAction', views.WriteExamAction, name="WriteExamAction"),	       
]