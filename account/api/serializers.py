from rest_framework import serializers
from django.conf.urls import url, include

from account.models import Account, Student, Teacher


class RegistrationSerializer(serializers.ModelSerializer): 

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'user_type', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email       = self.validated_data['email'],
            username    = self.validated_data['username'],
            user_type   = self.validated_data['user_type'],
            first_name  = self.validated_data['first_name'],
            last_name   = self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match !'})
        account.set_password(password)
        account.save()
        return account


class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username', 'user_type', 'first_name', 'last_name']
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['pk', 'user', 'student_id', 'first_name', 'last_name', 'institute', 'school', 'department', 'dptclass', 'status']


class UpdateStdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =  ['url', 'user', 'student_id', 'first_name', 'last_name', 'institute', 'school', 'department', 'dptclass']

    def validate_inst_id(self, pk):
        pprint(pk)

        existing = Student.objects.filter(id=pk).count()
        pprint(existing)

        if existing > 1:
            raise serializers.ValidationError('Student with this id exist')

        return abbr

    def validate(self, data): 
        pprint(data)
        return data