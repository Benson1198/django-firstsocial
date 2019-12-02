from django.contrib import admin
from . import models

class GorupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
