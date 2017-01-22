from __future__ import unicode_literals
from django.contrib import admin

from feedbacks.models import Feedback


# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Post model.
    list_display = ('next_country', 'created_at')
    search_fields = ('next_country',)

    # fieldsets = (
    #     (None, {'fields': ('title', 'link')}),
    #     (_('Writer'), {'fields': ('author')}),
    # )
    
    ordering = ('-created_at',)

# Now register the new Admin...
admin.site.register(Feedback, FeedbackAdmin)
