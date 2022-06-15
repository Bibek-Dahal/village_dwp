from django import forms
def check_mobile_num(attrs):
    if attrs.isnumeric():
        if len(attrs) == 10:
            return str(attrs)
    raise forms.ValidationError("Enter a valid phone number")