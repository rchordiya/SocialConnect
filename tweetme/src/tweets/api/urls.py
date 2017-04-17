from django.views.generic.base import RedirectView
from django.conf.urls import url
#from .views import TweetDetailView,TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView
from .views import TweetListAPIView
urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), #/tweet
]
