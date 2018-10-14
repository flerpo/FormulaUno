from django.contrib import admin

# Register your models here.
from Competition import models

admin.site.register(models.Results)
admin.site.register(models.Tracks)

