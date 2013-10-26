#from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms


class ContactForm(forms.Form):

    email = forms.EmailField(required=True,error_messages={'required': 'Pole wymagen', 'invalid': 'To nie jest e-mail'})
    message = forms.CharField(required=True,widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)