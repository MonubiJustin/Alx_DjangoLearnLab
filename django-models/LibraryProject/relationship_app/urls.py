from django.urls import path
from .views import book_list
from .views import LibraryDetailView

urlpatterns = [
    path("books/", views.book_list, name="book-list"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library-detail")
]
