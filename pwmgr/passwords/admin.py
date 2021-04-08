from django.contrib import admin
from .models import PasswordCategory, PasswordHint
# Register your models here.
admin.site.register(PasswordCategory)
admin.site.register(PasswordHint)