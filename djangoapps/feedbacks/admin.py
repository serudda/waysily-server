from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('uid', 'next_country', 'created_at')
    search_fields = ('next_country',)
    
    ordering = ('-created_at',)

admin.site.register(Feedback, FeedbackAdmin)
