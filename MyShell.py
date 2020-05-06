import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()  # these 4 lines are required for settings

from learning_logs.models import Topic

topics = Topic.objects.all() # puts in all objects related to Topic into variable topic

for topic in topics:
    print(topic.id, topic)

# if you know the id of a particular object, you can use the method Topic.objects.get()
# to retrieve that object and examine any attriubte the object has

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

# to get data thru a FK relationship, you use the lowercase name of the 
# related model followed by an underscore and the word set
entries = t.entry_set.all()

for entry in entries:
    print(entry)


from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)