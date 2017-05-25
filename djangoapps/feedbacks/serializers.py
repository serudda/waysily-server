from rest_framework import serializers
from djangoapps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Feedback model """

    class Meta:
        model = Feedback
        fields = ('id',
                  'next_country',
                  'next_feature',
                  'next_other_feature',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


