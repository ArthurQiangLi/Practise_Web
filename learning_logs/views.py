from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """main page of learning_logs"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """display all topics"""
    #topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    topics = Topic.objects.order_by('date_added') #lookup database, store to topics
    contex = {'topics':topics}
    return render(request, 'learning_logs/topics.html', contex)

@login_required
def topic(request, topic_id):
    """show single topic's all entry"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') #show latest first
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id):
    """add specific entry in a topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm() # new a empty form
    else:
        #Post submitted data
        form = EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)#false means create a new form object
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        #post submitted data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)