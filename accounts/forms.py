from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


#I am writing these forms solely for occasions when I might need a custom form.

class LoginForm(AuthenticationForm):
    pass


class CreateForm(UserCreationForm):
    pass