from rest_framework import serializers

from lil.models import student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name', 'username', 'password', 'DOB', 'Mark', ]