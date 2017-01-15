from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from early.models import Early


# Register your models here.
class EarlyAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Post model.
    list_display = ('first_name', 'last_name', 'email', 'comment', 'created_at')
    search_fields = ('email',)

    # fieldsets = (
    #     (None, {'fields': ('title', 'link')}),
    #     (_('Writer'), {'fields': ('author')}),
    # )
    
    ordering = ('-created_at',)


# Now register the new Admin...
admin.site.register(Early, EarlyAdmin)
