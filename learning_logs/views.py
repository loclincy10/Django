from django.shortcuts import render, redirect
# from .forms import TopicForm, EntryForm
from .forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

# When a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    # Show all topics
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #query to get only Topic objs from DB whose 
    #a context is a dictionary in which the keys are names we'll use         owner attribute matches current user
    # in the template to access the data, and the values are the data
    # we need to send to the template. In this case, there's one key-value pair
    # which contains the set of topics we'll display on the page
    context = {'topics':topics}
    #when building a page that uses data, we pass the context variable to render()
    # as well as the request object and the path to the template
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    #just like we did in MyShell.py
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    # foreign key can be accessed using '_set'
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form (create an instance of TopicForm)
        # Because we included no arguments when instantiating TopicForm, Djano
        # creates a blank form that the user can fill out
        form = TopicForm()
    else:
        # POST data submitted; process data
        # We make an instance of TopicForm and pass it the data entered by the user,
        # stored in request.POST.
        form = TopicForm(data=request.POST)
        #The is_valid() method checks that all required fields have been filled
        #in (all fields in a form are required by default) and that the data entered
        # matches the field types expected
        if form.is_valid():
            # write the data from the form to the DB
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # redirect the user's browser to the topics page
            return redirect('learning_logs:topics')
    
    # Display a blank form using hte new_topic.html template
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id) # getting the topic based on topic_id
    if request.method != 'POST': #if its a get method
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            # when we call save(), we include the argument commit=False to tell Django to create
            # a new entry object and assign it to new_entry without saving it to the database yet
            new_entry = form.save(commit=False) #commited the entry but didn't save to the DB
            # assign the topic of the new entry based on the topic we pulled from topic_id
            new_entry.topic = topic #we assign topic back to this variable
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    # Edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # this argument tells Django to create the form prefilled
        # with information from the existing entry object
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid(): # to make sure there's no malicious code
            form.save() # save it
            return redirect('learning_logs:topic', topic_id= topic.id) # we'll be redirected to the topics page
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context) # it renders the page based on the dictionary called context
