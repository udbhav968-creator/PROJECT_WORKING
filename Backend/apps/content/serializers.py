from rest_framework import serializers
from apps.content.models import (
    MedicalServiceModel,
    DoctorModel,
    BlogPostModel,
    TestimonialModel,
    GalleryImageModel,
    ContactInquiryModel,
)


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalServiceModel
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImageModel
        fields = '__all__'


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiryModel
        fields = '__all__'
