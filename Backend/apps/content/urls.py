from django.urls import path
from apps.content.views import (
    MedicalServiceListView,
    MedicalServiceDetailView,
    DoctorListView,
    DoctorDetailView,
    BlogPostListView,
    BlogPostDetailView,
    TestimonialListView,
    GalleryImageListView,
    ContactInquiryCreateView,
)

urlpatterns = [
    # Services APIs
    path('services/', MedicalServiceListView.as_view(), name='content-service-list'),
    path('services/<slug:slug>/', MedicalServiceDetailView.as_view(), name='content-service-detail'),

    # Doctors APIs
    path('doctors/', DoctorListView.as_view(), name='content-doctor-list'),
    path('doctors/<uuid:pk>/', DoctorDetailView.as_view(), name='content-doctor-detail'),

    # Blog APIs
    path('blogs/', BlogPostListView.as_view(), name='content-blog-list'),
    path('blogs/<slug:slug>/', BlogPostDetailView.as_view(), name='content-blog-detail'),

    # Testimonials APIs
    path('testimonials/', TestimonialListView.as_view(), name='content-testimonial-list'),

    # Gallery APIs
    path('gallery/', GalleryImageListView.as_view(), name='content-gallery-list'),

    # Contact Inquiry APIs
    path('contact/', ContactInquiryCreateView.as_view(), name='content-contact-create'),
]
