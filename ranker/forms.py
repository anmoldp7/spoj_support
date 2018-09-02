from django import forms

class user_handle_form(forms.Form):
    handle_name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={ "placeholder" : "Enter text", "class" : "handle-form"}))