from django.contrib import admin

# Register your models here.
from querysys.models import StdentInformation, StudentCourse, StudentScore

admin.site.register(StudentScore)
admin.site.register(StudentCourse)
admin.site.register(StdentInformation)
