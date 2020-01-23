from django.urls import path

from .import views

urlpatterns = [
    path('college/', views.CollegeView.as_view(), name='college1'),
    path('college/<int:pk>', views.CollegeView.as_view(), name='college2'),
    path('student/', views.StudentView.as_view(), name='student1'),
    path('student/<int:pk>/', views.StudentView.as_view(), name='student2')
]
