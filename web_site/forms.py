from django import forms

class ContactForm(forms.Form):

    name=forms.CharField(max_length=30,label="name",required=True)
    email=forms.EmailField(label="email",required=True)
    recom=forms.CharField(max_length=500,label="recom",required=True)
