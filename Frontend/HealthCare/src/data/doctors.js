import anjaliSharmaImage from "../assets/images/doctors/doctor-anjali-sharma.jpg";
import ayeshaKhanImage from "../assets/images/doctors/doctor-ayesha-khan.jpg";
import rahulMehtaImage from "../assets/images/doctors/doctor-rahul-mehta.jpg";

// Temporary frontend data.
// Replace this data with the backend API response after integration.

const doctors = [
  {
    id: 1,
    slug: "dr-anjali-sharma",
    name: "Dr. Anjali Sharma",
    specialization: "General Physician",
    qualification: "MBBS, MD – General Medicine",
    experience: "9+ Years Experience",
    image: anjaliSharmaImage,
    availability: "Mon – Sat",
    consultationTime: "10:00 AM – 4:00 PM",
    shortBio:
      "Experienced in primary healthcare, routine consultation, preventive guidance, and patient-focused treatment planning.",
    expertise: [
      "General Consultation",
      "Preventive Healthcare",
      "Routine Health Checkups",
    ],
    status: "Available Today",
  },
  {
    id: 2,
    slug: "dr-ayesha-khan",
    name: "Dr. Ayesha Khan",
    specialization: "Preventive Care Specialist",
    qualification: "MBBS, Diploma in Preventive Medicine",
    experience: "7+ Years Experience",
    image: ayeshaKhanImage,
    availability: "Tue – Sun",
    consultationTime: "11:00 AM – 5:00 PM",
    shortBio:
      "Focused on preventive healthcare, early risk identification, lifestyle improvement, and sustainable wellness planning.",
    expertise: [
      "Preventive Care",
      "Wellness Guidance",
      "Health Risk Assessment",
    ],
    status: "Available Today",
  },
  {
    id: 3,
    slug: "dr-rahul-mehta",
    name: "Dr. Rahul Mehta",
    specialization: "Internal Medicine Specialist",
    qualification: "MBBS, MD – Internal Medicine",
    experience: "11+ Years Experience",
    image: rahulMehtaImage,
    availability: "Mon – Fri",
    consultationTime: "9:30 AM – 3:30 PM",
    shortBio:
      "Specializes in long-term health management, diagnostic support, chronic conditions, and coordinated patient care.",
    expertise: [
      "Internal Medicine",
      "Chronic Care",
      "Diagnostic Support",
    ],
    status: "Limited Slots",
  },
];

export const doctorHighlights = [
  {
    id: 1,
    number: "3+",
    label: "Experienced Doctors",
  },
  {
    id: 2,
    number: "25+",
    label: "Years Combined Experience",
  },
  {
    id: 3,
    number: "6",
    label: "Healthcare Services",
  },
  {
    id: 4,
    number: "6 Days",
    label: "Weekly Availability",
  },
];

export const carePrinciples = [
  {
    id: 1,
    number: "01",
    title: "Patient-First Approach",
    description:
      "Every consultation begins with careful listening and a clear understanding of the patient’s concerns.",
  },
  {
    id: 2,
    number: "02",
    title: "Clear Medical Guidance",
    description:
      "Doctors explain health concerns and recommendations using simple, understandable language.",
  },
  {
    id: 3,
    number: "03",
    title: "Personalized Attention",
    description:
      "Healthcare guidance is tailored according to individual symptoms, history, and wellness goals.",
  },
];

export default doctors;