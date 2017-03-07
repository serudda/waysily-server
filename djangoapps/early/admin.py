from __future__ import unicode_literals
from django.contrib import admin
from djangoapps.early.models import Early


class EarlyAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email', 'comment', 'created_at')
    search_fields = ('email',)

    ordering = ('-created_at',)


admin.site.register(Early, EarlyAdmin)
