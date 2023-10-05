from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_managers
from django.core.mail import mail_admins


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Last name")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)
        subject='Welcome to news Board!',
        recipient_list=[user.email],
        message=f'{user.username}, You have successfully registered!',
        html = (
        f'<b>{user.username}</b>, You have successfully registered! '
        f'<a href="http://127.0.0.1:8000/News/"></a>!'),
        msg = EmailMultiAlternatives(
        body='text',
        from_email='None',
        to=[user.email]
        )
        msg.attach_alternative(html, message, "text/html"),
        msg.send()

        mail_managers(
            subject='New user!',
            message=f' user {user.username} have registered on the site.'
        )
        mail_admins(
            subject='New user!',
            message=f'user {user.username} have registered on the site.'
        )
        return user