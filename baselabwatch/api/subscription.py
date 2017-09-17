from baselabwatch.models import Subscription
from baselabwatch.serializers import SubscriptionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class SubscriptionViewSet(viewsets.ModelViewSet):
    "Viewsets for User reports."
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAdminUser,)