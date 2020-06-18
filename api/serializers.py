from rest_framework import serializers
from man.models import Man


class ManSerializers(serializers.ModelSerializer):
    class Meta:
        model = Man
        fields = '__all__'


class SendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Man
        fields = ('number', 'name', 'fname','role')

