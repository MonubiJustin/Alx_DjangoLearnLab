from . import views
from django.urls import path

urlpatterns = [
    path("books/", views.book_list, name="book-list"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library-detail")
]
