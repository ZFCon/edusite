from django import forms

from course.models import Course

class CreateCrseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ['ce_dptcls', 'ce_abb', 'ce_name'] 
		widgets ={ 
            'ce_abb': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'ce_abb',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'ce_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'ce_name',
                'required': True,
                'placeholder':'Course Name'
            }),
        }


class UpdateCrseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ['ce_dptcls', 'ce_abb', 'ce_name']

	def save(self, commit=True):
		crse = self.instance
		crse.abb = self.cleaned_data['ce_abb']
		crse.name = self.cleaned_data['ce_name']

		if commit:
			crse.save()
		return crse

