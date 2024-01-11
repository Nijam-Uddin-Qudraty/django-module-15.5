from django.urls import path 
from .import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('add_musician/',views.add_musician,name="add_musician"),
    path('add_album/',views.add_album,name="add_album"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
]
