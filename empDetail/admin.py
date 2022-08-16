from django.contrib import admin
from . models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'id', 'email', 'phone', 'department', 'role']

    list_filter = ['department', 'role']

    search_fields = ['name', 'username']

    list_editable = ['email']