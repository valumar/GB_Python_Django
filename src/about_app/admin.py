from django.contrib import admin
from .models import Work, Education, Organization

admin.site.register(Organization)
admin.site.register(Work)
admin.site.register(Education)
