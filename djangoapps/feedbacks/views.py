from rest_framework import viewsets
from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer


class FeedbackViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Feedback objects """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
