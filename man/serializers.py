from rest_framework.serializers import ModelSerializer
from .models import Man
from django.contrib.auth.models import User


class Order(ModelSerializer):
    class Meta:
        model = Man
        fields = ['number', 'name', 'fname', 'lname', 'address', 'birtday', 'passport', 'number_pass', 'body_pass',
                  'file', 'role', 'pin']


class UserRegistration(ModelSerializer):
    class Meta:
        model = Man
        fields = ['number', 'name', 'fname', 'lname', 'address', 'birtday', 'passport', 'number_pass', 'body_pass',
                  'file', 'role', 'pin']

    #     # def save(self, **kwargs):
    #     #     man = Man(
    #     #         name=self.validated_data['number'],
    #     #         pin=self.validated_data['pin']
    #     #     )
    #     #     user = User.objects.create_user(username=self.validated_data[], password=request.POST['pin'])
    #
    #
    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['number'], validated_data['pin'])
    #     return user

    def save(self, **kwargs):
        man = Man(
            name=self.validated_data['name'],
            lname=self.validated_data['lname'],
            fname=self.validated_data['fname'],
            address=self.validated_data['address'],
            birtday=self.validated_data['birday'],
            number_pass= self.validated_data['number_pass'],
            body_pass=self.validated_data['file'],
            role=self.validated_data['role'],
            pin=self.validated_data['pin']
        )
        man.save()
        return man