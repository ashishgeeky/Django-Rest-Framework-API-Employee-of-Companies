from rest_framework import serializers

from .models import company,myuser



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = (
            'id',
            'name',
            'city',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myuser
        fields = (
            'id',
            'firstname',
            'lastname',
            'age',
            'companyname',
        )
