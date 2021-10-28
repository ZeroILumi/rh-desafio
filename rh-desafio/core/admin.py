from django.contrib import admin

# Register your models here.
from core.models import Company, Employee, Department


class Employee_Admin(admin.ModelAdmin):
    list_display = ('id',
                    'department',
                    'name',
                    'gender',
                    'phone',
                    'role',
                    'age',
                    'joining_date',
                    'salary',)
    list_filter = ('department', 'name', 'role',)


class Company_Admin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'legal_number',)
    list_filter = ('name',)


class Department_Admin(admin.ModelAdmin):
    list_display = ('company',
                    'name',
                    'status',)
    list_filter = ('company',
                   'name',
                   'status',)


admin.site.register(Employee, Employee_Admin)
admin.site.register(Company, Company_Admin)
admin.site.register(Department, Department_Admin)
