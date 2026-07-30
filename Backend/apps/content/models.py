from django.db import models
from apps.core.models import TimeStampedModel


class MedicalServiceModel(TimeStampedModel):
    """
    Module 3: Medical Services & Clinical Specialties Catalog Model
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    category = models.CharField(max_length=100, default='General')
    description = models.TextField()
    full_details = models.TextField(blank=True, null=True)
    icon_name = models.CharField(max_length=100, default='Stethoscope')
    image_url = models.URLField(blank=True, null=True)
    consultation_fee_inr = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    is_featured = models.BooleanField(default=True)

    class Meta:
        db_table = 'medical_services'

    def __str__(self):
        return f"{self.title} (₹{self.consultation_fee_inr})"


class DoctorModel(TimeStampedModel):
    """
    Module 3: Board-Certified Doctors & Specialists Directory Model
    """
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255, default='MBBS, MD')
    experience_years = models.IntegerField(default=10)
    bio = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    consultation_fee_inr = models.DecimalField(max_digits=10, decimal_places=2, default=600.00)
    opd_timings = models.CharField(max_length=100, default='09:00 AM - 05:00 PM')
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'doctors'

    def __str__(self):
        return f"{self.name} - {self.specialty}"


class BlogPostModel(TimeStampedModel):
    """
    Module 3: Medical Health Blog Articles & Patient Education Model
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.CharField(max_length=255, default='Dr. Divit Shah')
    category = models.CharField(max_length=100, default='Preventive Health')
    summary = models.TextField()
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = 'blog_posts'

    def __str__(self):
        return f"{self.title} by {self.author}"


class TestimonialModel(TimeStampedModel):
    """
    Module 3: Patient Feedback, Reviews & Testimonials Model
    """
    patient_name = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255, default='General OPD Care')
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)

    class Meta:
        db_table = 'testimonials'

    def __str__(self):
        return f"{self.patient_name} - {self.rating}★"


class GalleryImageModel(TimeStampedModel):
    """
    Module 3: Medical Facility & Clinical Infrastructure Gallery Model
    """
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='Facility')
    image_url = models.URLField()
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'gallery_images'

    def __str__(self):
        return f"{self.title} ({self.category})"


class ContactInquiryModel(TimeStampedModel):
    """
    Module 3: Patient Contact Inquiries & Helpdesk Messages Model
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)

    class Meta:
        db_table = 'contact_inquiries'

    def __str__(self):
        return f"Inquiry from {self.full_name}: {self.subject}"
