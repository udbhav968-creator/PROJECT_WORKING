from django.contrib import admin
from apps.content.models import (
    MedicalServiceModel,
    DoctorModel,
    BlogPostModel,
    TestimonialModel,
    GalleryImageModel,
    ContactInquiryModel,
)


@admin.register(MedicalServiceModel)
class MedicalServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'consultation_fee_inr', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category')


@admin.register(DoctorModel)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'qualifications', 'consultation_fee_inr', 'is_available')
    search_fields = ('name', 'specialty')


@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author')


@admin.register(TestimonialModel)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'treatment', 'rating', 'is_approved')
    list_filter = ('rating', 'is_approved')


@admin.register(GalleryImageModel)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_url')


@admin.register(ContactInquiryModel)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'is_resolved', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    readonly_fields = ('created_at',)
