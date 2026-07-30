from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from apps.content.models import (
    MedicalServiceModel,
    DoctorModel,
    BlogPostModel,
    TestimonialModel,
    GalleryImageModel,
    ContactInquiryModel,
)
from apps.content.serializers import (
    MedicalServiceSerializer,
    DoctorSerializer,
    BlogPostSerializer,
    TestimonialSerializer,
    GalleryImageSerializer,
    ContactInquirySerializer,
)


class MedicalServiceListView(ListAPIView):
    """
    Module 3: List All Medical Services & Clinical Specialties
    """
    queryset = MedicalServiceModel.objects.filter(is_featured=True).order_by('title')
    serializer_class = MedicalServiceSerializer
    permission_classes = [permissions.AllowAny]


class MedicalServiceDetailView(RetrieveAPIView):
    """
    Module 3: Retrieve Detailed Medical Service by Slug
    """
    queryset = MedicalServiceModel.objects.all()
    serializer_class = MedicalServiceSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class DoctorListView(ListAPIView):
    """
    Module 3: List Board-Certified Doctors & Specialists
    """
    queryset = DoctorModel.objects.filter(is_available=True).order_by('-experience_years')
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]


class DoctorDetailView(RetrieveAPIView):
    """
    Module 3: Retrieve Doctor Detail by Primary Key
    """
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.AllowAny]


class BlogPostListView(ListAPIView):
    """
    Module 3: List Medical Blog Posts & Articles
    """
    queryset = BlogPostModel.objects.filter(is_published=True).order_by('-published_date')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]


class BlogPostDetailView(RetrieveAPIView):
    """
    Module 3: Retrieve Blog Article by Slug
    """
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class TestimonialListView(ListAPIView):
    """
    Module 3: List Approved Patient Testimonials & Reviews
    """
    queryset = TestimonialModel.objects.filter(is_approved=True).order_by('-rating')
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]


class GalleryImageListView(ListAPIView):
    """
    Module 3: List Medical Facility & Clinical Infrastructure Gallery Images
    """
    queryset = GalleryImageModel.objects.all().order_by('-created_at')
    serializer_class = GalleryImageSerializer
    permission_classes = [permissions.AllowAny]


class ContactInquiryCreateView(CreateAPIView):
    """
    Module 3: Submit Patient Contact Inquiry & Helpdesk Message
    """
    queryset = ContactInquiryModel.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "success": True,
            "message": "Thank you for contacting Pure Health Clinic. Our patient helpdesk will get in touch shortly.",
            "inquiry": serializer.data
        }, status=status.HTTP_201_CREATED)
