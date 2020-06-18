from django.contrib import admin
from .models import Man

admin.site.site_header = 'Эл каттоо 2020-жыл'


class Users(admin.ModelAdmin):
    list_display = [field.name for field in Man._meta.fields]
    fields = ['number', 'fname', 'name', 'lname', 'address', 'birtday', 'passport', 'number_pass', 'body_pass', 'pin',
            'file','role', 'user']
    list_filter = ['role']
    search_fields = ['name', 'role', 'number', 'number_pass']
    # ordering = ['role', 'number']

    class Meta:
        model = Man


admin.site.register(Man, Users)
