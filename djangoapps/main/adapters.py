from allauth.account.adapter import DefaultAccountAdapter


class MessageFreeAdapter(DefaultAccountAdapter):
    """
    django-allauth's `allauth.account.adapter.DefaultAccountAdapter` uses Django's messaging middleware to give
    feedback to users. When using django-rest-auth for registration/login JSON-REST requests a traceback is
    generated when the `HTTPRequest` is passed into `django.contrib.messages.add_messages` when a `Request`
    is expected:

    Exception Type: TypeError at /rest-auth/registration/
    Exception Value: add_message() argument must be an HttpRequest object, not &#39;Request&#39;.

    If messaging cannot be disabled (it is used by other applications) using this subclass
    disables messaging for allauth/django-rest-auth.

    In settings.py add ACCOUNT_ADAPTER = 'main.adapters.MessageFreeAdapter'
    """
    def add_message(self, request, level, message_template,
                    message_context={}, extra_tags=''):
        pass
