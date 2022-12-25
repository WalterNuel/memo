from django.contrib import admin
from .models import Profile, Note, Task
# Register your models here.
admin.site.register(Profile)
admin.site.register(Note)
admin.site.register(Task)