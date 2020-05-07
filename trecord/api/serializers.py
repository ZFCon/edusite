from rest_framework import serializers 

from trecord.models import TRecord

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRecord
        fields = (
            'std_inst', 'std_sch', 'std_dept', 'std_dptcls', 'std_id', 'std_abbr', 'std_fname', 'std_lname'
        )

    def validate_std_abbr(self, abbr):
        pprint(abbr)

        existing = TRecord.objects.filter(std_abbr=abbr).count()

        if existing > 0:
            raise serializers.ValidationError('Student with this id exist')

        return abbr

    def validate(self, data):
        return data


class UpdateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRecord
        fields = (
            'std_inst', 'std_sch', 'std_dept', 'std_dptcls', 'std_abbr', 'std_fname', 'std_lname'
        )

    def validate_std_abbr(self, abbr):
        pprint(abbr)

        existing = TRecord.objects.filter(std_abbr=abbr).count()
        pprint(existing)

        if existing > 1:
            raise serializers.ValidationError('Student with this id exist')

        return abbr

    def validate(self, data):
        pprint(data)
        return data
