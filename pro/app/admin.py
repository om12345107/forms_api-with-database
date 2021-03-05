from django.contrib import admin
from app.models import jock
# Register your models here.
@admin.register(jock)

class nope(admin.ModelAdmin):
    list_display=('name','mobile','city','email','password')

