from django import forms

from institute.models import Institute 
from department.models import Department
from dptclass.models import DptClass


class CreateDptclsForm(forms.ModelForm):

	class Meta:
		model = DptClass
		fields = ['dcls_dpt', 'dcls_abb', 'dcls_name'] 
		widgets ={ 
            'dcls_abb': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'dcls_abb',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'dcls_name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'dcls_name',
                'required': True,
                'placeholder':'Class Name'
            }),
        }


class UpdateDptclsForm(forms.ModelForm):

	class Meta:
		model = DptClass
		fields = ['dcls_dpt', 'dcls_abb', 'dcls_name']

	def save(self, commit=True):
		dptcls = self.instance
		dptcls.abb = self.cleaned_data['dcls_abb']
		dptcls.name = self.cleaned_data['dcls_name']

		if commit:
			dptcls.save()
		return dptcls

