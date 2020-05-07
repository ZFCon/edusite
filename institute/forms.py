from django import forms

from institute.models import Institute 


class CreateInstForm(forms.ModelForm): 

	class Meta:
		model = Institute
		fields = ['abb', 'name']
		widgets ={ 
            'abb': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'inst-abb',
                'required': True,
                'placeholder':'Abbreviation'
            }),
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'id': 'inst-name',
                'required': True,
                'placeholder':'Institute Name'
            }),
        }


class UpdateInstForm(forms.ModelForm):

	class Meta:
		model = Institute
		fields = ['abb', 'name']

	def save(self, commit=True):
		inst = self.instance
		inst.abb = self.cleaned_data['abb']
		inst.name = self.cleaned_data['name']

		if commit:
			inst.save()
		return inst

