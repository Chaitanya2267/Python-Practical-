
import re
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{2,19}', username):
            raise forms.ValidationError(
                "Username must start with a letter and contain 3-20 letters, numbers, or underscores."
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if not re.fullmatch(pattern, password):
            raise forms.ValidationError(
                "Password must contain 8+ characters, uppercase, lowercase, digit, and special character."
            )

        return password
