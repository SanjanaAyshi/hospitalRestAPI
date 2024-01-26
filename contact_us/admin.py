from django.contrib import admin
from .models import ContactUs
# Register your models here.

#list_display database e table akare ki ki section thakbe ta dekhabe.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']
#list_display creat korar por ta pass kore ditehoi
admin.site.register(ContactUs, ContactModelAdmin)