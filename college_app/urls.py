from django.urls import path

#from college_app import views
from  .import views

urlpatterns = [
    path('college/', views.CollegeView.as_view(), name='college'),
    path('college/<int:pk>', views.CollegeView.as_view(), name='college'),
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentView.as_view(), name='student')
]
