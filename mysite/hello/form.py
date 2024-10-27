from django import forms
from .models import Friend, Message

class HelloForm(forms.Form):
    name=forms.IntegerField(label="name",widget=forms.TextInput(attrs={"class":"form-control"}))
    mail=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    gender=forms.BooleanField(label="gender",required=False,widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    age=forms.IntegerField(label="age",widget=forms.NumberInput(attrs={"class":"form-control"}))
    birthday=forms.DateField(label="birthday",widget=forms.DateInput(attrs={"class":"form-control"}))
    #choice=forms.ChoiceField(label="choice",choices=data)

class SessionForm(forms.Form):
    session=forms.CharField(label="session",required=False,widget=forms.TextInput(attrs={"class":"form-control"}))

class FriendForm(forms.ModelForm):
    class Meta:
        model=Friend
        fields=["name","mail","gender","age","birthday"]

class FindForm(forms.Form):
    find=forms.CharField(label="Find",required=False,widget=forms.TextInput(attrs={"class":"form-control"}))

class CheckForm(forms.Form):
    str=forms.CharField(label="name",widget=forms.TextInput(attrs={"class":"form-control"}))

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields =["title","content","friend"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control form-control-sm"}),
            "content":forms.Textarea(attrs={"class":"form-control form-control-sm","rows":2}),
            "friend":forms.Select(attrs={"class":"form-control form-control-sm"})
        }