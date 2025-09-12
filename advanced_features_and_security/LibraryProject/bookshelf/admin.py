from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "email",
        "username",
        "date_of_birth",
        "is_staff"
    ]
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                "date_of_birth",
            ),
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                "date_of_birth",
            ),
        }),
    )
    

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)