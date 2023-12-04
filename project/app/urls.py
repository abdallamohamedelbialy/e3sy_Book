from django.urls import path
from .import views 

urlpatterns = [
    path('', views.Abdalla, name='app1'),
    path('book', views.Omer, name='app2'),
    path('up/<int:id>', views.fatma, name='app3'),
    path('del/<int:id>', views.abdelrahman, name='app4'),
]


