
from rest_framework import serializers

from loginApp.models import *



        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisterTable
        fields = ['name', 'email', 'password']
                
 # Normal serializers -----------       
# class RegisterSerializer(serializers.Serializer):
#                name = serializers.CharField(max_length=50)
#                email = serializers.EmailField()
#                password = serializers.CharField(max_length=100)

#     # Optional: You can add custom validation methods if needed
# def validate_email(self, value):
        
#         if 'example' in value:
#             raise serializers.ValidationError("Email cannot contain 'example'.")
#         return value
# def validate_password(self, value):
#         # Add custom password validation logic
#         if len(value) < 8:
#             raise serializers.ValidationError("Password must be at least 8 characters long.")
#         return value