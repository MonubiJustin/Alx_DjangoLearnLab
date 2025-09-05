from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("register/", views.register, name="register"),
    # path("login/", login_view, name="login"),
    # path("logout/", logout_view, name="logout")
    # 🔹 Login using Django’s built-in LoginView
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # 🔹 Logout using Django’s built-in LogoutView
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
