from django import forms
from .models import Student, Society, Event, Review, Membership
from django.contrib.auth.models import User


class LogInForm(forms.ModelForm):
	
	class Meta:
		
		model = Student
		fields = ('username','password')
	
	
	
class SocietyForm(forms.ModelForm):

    name = forms.CharField(max_length = 128, help_text = "Please enter the name of the society")
    description = forms.CharField(widget = forms.Textarea)
    email = forms.EmailField(widget = forms.EmailInput)
    facebook = forms.URLField(widget = forms.URLInput)
    twitter = forms.URLField(widget = forms.URLInput)
    linkedin = forms.URLField(widget = forms.URLInput)
    instagram = forms.URLField(widget = forms.URLInput)

    class Meta:
        
        model = Society
        exclude = ('members',)


class EventForm(forms.ModelForm):

    name = forms.CharField(max_length = 128, help_text = "Please enter the name of the event")
    date = forms.CharField(widget = forms.DateInput)
    time = forms.CharField(widget = forms.TimeInput)
    description = forms.CharField(widget = forms.Textarea)
    image = forms.ImageField()

    class Meta:

        model = Event
        exclude = ('attended_by', 'organized_by',)


class ReviewForm(forms.ModelForm):

    rating = forms.IntegerField(max_value = 10, min_value = 0)
    description = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Review
        exclude = ('event', 'made_by')



class MemberForm(forms.ModelForm):
	
    class Meta:
        model = Student
        fields = ('matricNo', 'username', 'password', 'picture', 'year', 'degree')
