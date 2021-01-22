

from django.contrib import admin

from .models import Events
from .models import Sessions

# Register your models here.
admin.site.register(Sessions)
admin.site.register(Events)
