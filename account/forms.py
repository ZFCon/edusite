from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account, Student


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('user_type', 'first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)


class CreateStdForm(forms.ModelForm): 
	class Meta:
		model = Student
		fields = ['student_id', 'first_name', 'last_name', 'school', 'department', 'dptclass']
		widgets ={ 
            'student_id': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'std-id',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'std-fname',
                'required': True,
                'placeholder':'First Name'
            }),
			'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'std-lname',
                'required': True,
                'placeholder':'Last Name'
            }),
			'school': forms.Select(attrs={
                'class':'form-control',
                'id': 'std-sch',
				'placeholder':'School'
            }),
            'department': forms.Select(attrs={
                'class':'form-control',
                'id': 'std-dept',
				'placeholder':'Department'
            }),
            'dptclass': forms.Select(attrs={
                'class':'form-control',
                'id': 'std-dptcls',
				'placeholder':'Class'
            }),
        }


class UpdateStdForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['student_id', 'first_name', 'last_name' ]

	def save(self, commit=True):
		std = self.instance
		std.id = self.cleaned_data['student_id']
		std.fname = self.cleaned_data['first_name']
		std.lname = self.cleaned_data['last_name']

		if commit:
			std.save()
		return std


















