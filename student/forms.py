from django import forms
from account.models import Student
from .models import Student as StudentCourses

class UpdateStdCrseForm(forms.ModelForm):
    class Meta:
        model = StudentCourses
        fields = ['student_id', 'course']
        widgets ={ 
            'student_id': forms.TextInput(attrs={
            'class':'form-control',
            'id': 'std-id',
            'required': True,
            'placeholder':'Abbreviation'
            }),
            'course': forms.SelectMultiple(attrs={
            'class':'form-control',
            'id': 'course',
            'required': True,
            }),
            }

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
        }


class UpdateStdForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['student_id', 'first_name', 'last_name', 'school', 'department', 'dptclass', ]

	def save(self, commit=True):
		std = self.instance
		std.id = self.cleaned_data['student_id']
		std.fname = self.cleaned_data['first_name']
		std.lname = self.cleaned_data['last_name']

		if commit:
			std.save()
		return std

