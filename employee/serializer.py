from rest_framework import serializers
from .models import *



class EmployeeSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField()

    def validate_photo(self, value):
        
        if value.size > 5 * 1024 * 1024: 
            raise serializers.ValidationError("Image file size should not exceed 5 MB.")
        return value
    

    class Meta:

        model = Employee
        fields = "__all__"
    
