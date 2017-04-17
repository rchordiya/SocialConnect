from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetModelSerialzier

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerialzier

    def get_queryset(self):
        return Tweet.objects.all()
