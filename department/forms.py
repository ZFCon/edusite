from django import forms

from institute.models import Institute 
from department.models import Department


class CreateDeptForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = ['dpt_sch', 'dpt_abb', 'dpt_name']
		widgets ={ 
            'dpt_abb': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'dpt_abb',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'dpt_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'dpt_name',
                'required': True,
                'placeholder':'Department Name'
            }),
        }


class UpdateDeptForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = ['dpt_sch', 'dpt_abb', 'dpt_name']

	def save(self, commit=True):
		dpt = self.instance
		dpt.abb = self.cleaned_data['dpt_abb']
		dpt.name = self.cleaned_data['dpt_name']

		if commit:
			dpt.save()
		return dpt

