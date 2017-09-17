from logger.models import PollQuestion, PollChoice
from logger.serializers import PollQuestionSerializer, PollChoiceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class PollQuestionViewSet(viewsets.ModelViewSet):
    "Viewsets for PollQuestions."
    queryset = PollQuestion.objects.all()
    serializer_class = PollQuestionSerializer
    permission_classes = (IsAdminUser,)

class PollChoiceViewSet(viewsets.ModelViewSet):
    "Viewsets for PollChoices."
    queryset = PollChoice.objects.all()
    serializer_class = PollChoiceSerializer
    permission_classes = (IsAdminUser,)