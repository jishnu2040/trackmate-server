# Validation and serialization

from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    # write_only= True, because password no need to deserialize
    password=serializers.CharField(max_length =68, min_length =6, write_only =True)
    password2=serializers.CharField(max_length =68, min_length =6, write_only =True)
    

    class Meta:
        model = User
        fields = ('email','username', 'password', 'password2', 'is-active', 'is_staff', 'is_superuser')