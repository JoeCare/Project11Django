from django import forms


class PostItemForm(forms.Form):
    name = forms.CharField(label='Item name', max_length=30)
    type = forms.CharField(label='Item type', max_length=30)
    value = forms.IntegerField(label='Estimated value')
    image = forms.CharField(label='Example image url', max_length=1000, required=False)
