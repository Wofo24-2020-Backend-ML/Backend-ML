from rest_framework import serializers 
from account.models import *
from django.contrib.auth.models import User

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['category']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']

# class PackageSerializer(serializers.ModelSerializer):
#     user = UserSerializer(required=True)
#     category = serializers.StringRelatedField(many=False)
#     class Meta:
#         model = Package
#         fields = ['id', 'user', 'package_name', 'category', 'about', 'package_image', 'cost', 'cost_factor']
     




class PackageSerializer1(serializers.ModelSerializer): 
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Package
        fields = ['id', 'user', 'package_name', 'about', 'package_image', 'cost', 'cost_factor']


class CategorySerializer(serializers.ModelSerializer):
    packages = PackageSerializer1(many=True, read_only=True, source='package_set')
    class Meta:
        model = Category
        fields = ['id', 'category', 'packages']


class PackageSerializer(serializers.ModelSerializer): 
    user = serializers.ReadOnlyField(source='user.username')
    category = serializers.SlugRelatedField(many=False, queryset=Category.objects.all(), slug_field='category')
    class Meta:
        model = Package
        fields = ['id', 'user', 'package_name', 'category', 'about', 'package_image', 'cost', 'cost_factor']


class ProfessionalSerializer(serializers.ModelSerializer):
    sub_category = serializers.SlugRelatedField(many=True, queryset=SubCategory.objects.all(), slug_field='subcategory')
    class Meta:
        model = Professional
        fields = ['sub_category', 'business_name', 'phone_no', 'job_completed', 'address', 'service_charge', 'logo', 'joining_date']


class UserSerializer(serializers.ModelSerializer):
    professional = ProfessionalSerializer(required = True, many = False)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'professional']

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )

        professional_data = validated_data.pop('professional')
        professional = Professional.objects.create(
            user = user,
            sub_category = professional_data['sub_category'],
            business_name = professional_data['business_name'],
            phone_no = professional_data['phone_no'],
            job_completed = professional_data['job_completed'],
            address = professional_data['address'],
            service_charge = professional_data['service_charge'],
            logo = professional_data['logo']
        )
        return user
    
class UploadImageSerializer1(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ['id', 'image']


# class UploadImageSerializer(serializers.ModelSerializer):
#     image = UploadImageSerializer1(many=True, read_only=True, source='uploadimage_set')
#     username = serializers.ReadOnlyField()
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'image']


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UploadImage
        fields = ['user', 'image']