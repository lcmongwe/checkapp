from django.contrib import admin
from .models import *
from .forms import RegisterUserForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model= User
    add_form=RegisterUserForm

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Neighborhood)


