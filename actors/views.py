from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
