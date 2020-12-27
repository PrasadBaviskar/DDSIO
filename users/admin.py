from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserModel)
admin.site.register(Profile)
admin.site.register(Notes)
admin.site.register(Question_Papers)
admin.site.register(Model_Papers)
admin.site.register(Quiz)
admin.site.register(Institute)