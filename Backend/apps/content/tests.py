from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.content.models import (
    MedicalServiceModel,
    DoctorModel,
    BlogPostModel,
    TestimonialModel,
    ContactInquiryModel,
)


class ContentModuleTests(APITestCase):
    def setUp(self):
        self.service = MedicalServiceModel.objects.create(
            title="Cardiology Care",
            slug="cardiology-care",
            category="Cardiology",
            description="Comprehensive Heart Health Care",
            consultation_fee_inr=1000.00
        )
        self.doctor = DoctorModel.objects.create(
            name="Dr. Rahul Mehta",
            specialty="Cardiologist",
            qualifications="MBBS, MD Cardiology",
            experience_years=15,
            bio="Senior Cardiologist",
            consultation_fee_inr=1000.00
        )
        self.blog = BlogPostModel.objects.create(
            title="Heart Health Tips",
            slug="heart-health-tips",
            summary="Essential heart tips",
            content="Full article content"
        )
        self.testimonial = TestimonialModel.objects.create(
            patient_name="Suresh Kumar",
            treatment="Cardiology OPD",
            rating=5,
            comment="Excellent care"
        )

    def test_list_services(self):
        response = self.client.get(reverse('content-service-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_list_doctors(self):
        response = self.client.get(reverse('content-doctor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_list_blogs(self):
        response = self.client.get(reverse('content-blog-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_testimonials(self):
        response = self.client.get(reverse('content-testimonial-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_submit_contact_inquiry(self):
        payload = {
            "full_name": "Ramesh Gupta",
            "email": "ramesh@example.com",
            "phone": "+91 9811122233",
            "subject": "OPD Consultation Inquiry",
            "message": "I would like to inquire about OPD timings."
        }
        response = self.client.post(reverse('content-contact-create'), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ContactInquiryModel.objects.filter(email="ramesh@example.com").exists())
