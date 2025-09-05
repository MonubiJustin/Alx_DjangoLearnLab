from django.urls import path
from .views import list_books
from .views import LibraryDetailView, register_view, login_view, logout_view

urlpatterns = [
    path("books/", list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout")
]
