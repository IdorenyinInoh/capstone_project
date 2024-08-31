# Register your models here.
from django.contrib import admin
from .models import Staff, Attendance, DutyPost

admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(DutyPost)
