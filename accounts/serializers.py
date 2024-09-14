# Validation and serialization
from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    # write_only= True, because password no need to deserialize
    password=serializers.CharField(max_length =68, min_length =6, write_only =True)
    password2=serializers.CharField(max_length =68, min_length =6, write_only =True)
    

    class Meta:
        model = User
        fields = ('email','username', 'password', 'password2', 'is_active', 'is_staff', 'is_superuser')

    

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password2', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

  
    