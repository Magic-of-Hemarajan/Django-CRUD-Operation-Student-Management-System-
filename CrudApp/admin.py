from django.contrib import admin
from CrudApp.models import StudentModels
# Register your models here.
class StudentModelsAdmin(admin.ModelAdmin):
    list = '__all__'
admin.site.register(StudentModels,StudentModelsAdmin)

