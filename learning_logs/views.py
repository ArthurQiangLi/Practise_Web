from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    """main page of learning_logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """display all topics"""
    topics = Topic.objects.order_by('date_added') #lookup database, store to topics
    contex = {'topics':topics}
    return render(request, 'learning_logs/topics.html', contex)

def topic(request, topic_id):
    """show single topic's all entry"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') #show latest first
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """add usr's new topic"""
    if request.method != 'POST': #this is GET
        form = TopicForm() # if not submitting a form, new a form
        print('new topic Get')
    else:# this is POST
        print('new topic POST')
        #POST submitted data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)