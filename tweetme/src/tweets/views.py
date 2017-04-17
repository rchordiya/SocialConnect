from django import forms
from django.forms.utils import ErrorList
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView,UpdateView, DeleteView
from .forms import TweetModelForm
# Create your views here.
from django.shortcuts import render
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model=Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    #success_url = "/tweet/"

class TweetCreateView(FormUserNeededMixin, UserOwnerMixin,CreateView):
    form_class= TweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = reverse_lazy("tweet:detail")



class TweetDetailView(DetailView):
    queryset= Tweet.objects.all()
    #template_name = "tweets/detail_view.html"

class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        print(self.request.GET)
        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
    def get_context_data(self, *args, **kwargs):
        context=super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form']=TweetModelForm()
        context['create_url']= reverse_lazy("tweet:create")
        return context

"""
def tweet_detail_view(request,id=1):
    obj= Tweet.objects.get(id=id) # Getting from database
    #print(obj)
    context={
        "object":obj
    }
    return render(request,"tweets/detail_view.html",context)

def tweet_list_view(request):
    queryset=Tweet.objects.all()
    print(queryset)
    context={
        "object_list":queryset
    }
    return render(request,"tweets/list_view.html",context)
"""
