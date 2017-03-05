from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from djangoapps.feedbacks.models import Feedback
from djangoapps.feedbacks.serializers import FeedbackSerializer


class FeedbackViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Feedback objects """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (AllowAny,)
