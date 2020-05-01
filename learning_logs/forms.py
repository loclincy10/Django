from django import forms

from .models import Topic, Entry #.models means looks for models.py in the same directory

class TopicForm(forms.ModelForm):
    class Meta: # meta class allows us to access forms in our DB
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # a widget is an HTML form element, such as a single-line box,
        # multi-line text area, or drop-down list.
        # customize the input widget for the field 'text' so the text area
        # will be 80 columns wide instead of the default 40
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
