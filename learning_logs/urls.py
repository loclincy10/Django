
#the path functino, which is needed when mapping URLs to views
from django.urls import path

# the dot tells Python to import the views.py module from
# the same directory as teh current urls.py module
from . import views 

#the variable app_name helps Django distinguish this urls.py file from
# files of the same name in other apps within the project
app_name = 'learning_logs'

#the variable urlpatterns in this module is a list of individual pahes
#that can be requested from the learning_logs app
urlpatterns = [
    #the first arg is an empty string ('') which matches the
    #base URL - http://localhost:8000/. the second arg specifies 
    # the functino name to callin views.py. The third arguemtn provides
    # the name 'index' for this URL pattern to refer to it later
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    # the integer value is stored in the variable topic_id and will
    # be subsequently passed to the topic function in views.py
    path('topics/<int:topic_id>/', views.topic,name='topic'), # we created a variable called topic_id, so it's dynamic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]