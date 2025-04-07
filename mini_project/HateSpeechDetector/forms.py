from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput())
    mode = forms.ChoiceField(choices=(('lstm2x', 'lstm2x'), ('model2', 'model2'),('model3','model3')))


