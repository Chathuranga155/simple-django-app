from django import forms
from .models import GeeksModel


from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {'email': 'Email'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    

class GeeksForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = GeeksModel

		# specify fields to be used
		fields = [
			"title",
			"description",
		]

