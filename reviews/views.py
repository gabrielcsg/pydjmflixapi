from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewCreateListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
