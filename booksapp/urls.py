from django.urls import path
from .views import *

urlpatterns = [
  path('',bookList, name="booklist"),
  path('book/<int:id>',bookDetals, name="bookdetails"),
]