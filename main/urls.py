from django.urls import path

from main import views

urlpatterns = [
    path("books/", views.BookList.as_view()),
    path("books/<int:pk>/", views.BookDetail.as_view()),
]
