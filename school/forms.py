from django import forms

from institute.models import Institute 
from school.models import School


class CreateSchForm(forms.ModelForm):

	class Meta:
		model = School
		fields = ['sch_inst', 'sch_abb', 'sch_name']
		widgets ={ 
            'sch_abb': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'sch_abb',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'sch_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'sch_name',
                'required': True,
                'placeholder':'School Name'
            }),
        }


class UpdateSchForm(forms.ModelForm):

	class Meta:
		model = School
		fields = ['sch_inst', 'sch_abb', 'sch_name']

	def save(self, commit=True):
		sch = self.instance
		sch.abb = self.cleaned_data['sch_abb']
		sch.name = self.cleaned_data['sch_name']

		if commit:
			sch.save()
		return sch

