#-*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView

from .forms import ContactForm


class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = "/sent/"

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        mail_subject = "Msg from {0}".format(name)
        mail_message = "{0} / {1}: \n\n{2}".format(name, email, message)
        send_mail(
            subject=mail_subject,
            message=mail_message,
            from_email=settings.CONTACT_FROM_EMAIL,
            recipient_list=settings.EMAIL_RECIPIENTS.split(',')
        )

        return super(ContactFormView, self).form_valid(form)