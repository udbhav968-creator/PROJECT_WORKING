import generalConsultationImage from "../assets/images/services/general-consultation.jpg";
import preventiveCareImage from "../assets/images/services/preventive-care.jpg";
import healthCheckupImage from "../assets/images/services/health-checkup.jpg";
import diagnosticSupportImage from "../assets/images/services/diagnostic-support.jpg";
import chronicCareImage from "../assets/images/services/chronic-care.jpg";
import wellnessGuidanceImage from "../assets/images/services/wellness-guidance.jpg";

// Temporary frontend data.
// Replace this data with the backend API response after integration.

const services = [
  {
    id: 1,
    slug: "general-consultation",
    title: "General Consultation",
    category: "Primary Care",
    shortDescription:
      "Professional medical consultation for common health concerns, symptoms, and routine healthcare guidance.",
    description:
      "Our general consultation service provides patients with a comfortable and reliable environment to discuss symptoms, health concerns, and everyday medical needs. The consultation focuses on understanding the patient’s condition, reviewing relevant medical history, and recommending the appropriate next steps.",
    image: generalConsultationImage,
    icon: "01",
    duration: "20–30 minutes",
    availability: "Monday to Saturday",
    suitableFor: [
      "Fever, cold, cough, and common infections",
      "Headache, fatigue, or general weakness",
      "Digestive discomfort and minor health concerns",
      "Routine medical advice and follow-up consultation",
    ],
    benefits: [
      "Personalized medical assessment",
      "Clear explanation of possible health concerns",
      "Responsible treatment recommendations",
      "Referral guidance when specialist care is required",
    ],
    process: [
      {
        title: "Initial Discussion",
        description:
          "The doctor listens to your symptoms, medical concerns, and relevant health history.",
      },
      {
        title: "Clinical Assessment",
        description:
          "A professional evaluation is conducted based on the information and symptoms provided.",
      },
      {
        title: "Care Recommendation",
        description:
          "You receive clear guidance, treatment recommendations, and follow-up instructions.",
      },
    ],
  },
  {
    id: 2,
    slug: "preventive-care",
    title: "Preventive Care",
    category: "Health Prevention",
    shortDescription:
      "Proactive healthcare guidance designed to identify health risks early and support long-term well-being.",
    description:
      "Preventive care focuses on maintaining good health and reducing the possibility of future health complications. Through regular assessment, lifestyle guidance, and early risk identification, patients can make informed decisions about their long-term health.",
    image: preventiveCareImage,
    icon: "02",
    duration: "30–40 minutes",
    availability: "Monday to Friday",
    suitableFor: [
      "Individuals seeking long-term health planning",
      "Patients with a family history of medical conditions",
      "Adults requiring routine preventive assessment",
      "People interested in healthier lifestyle practices",
    ],
    benefits: [
      "Early identification of potential health risks",
      "Personalized preventive healthcare planning",
      "Lifestyle and wellness recommendations",
      "Better understanding of personal health indicators",
    ],
    process: [
      {
        title: "Risk Review",
        description:
          "We review your medical history, family history, lifestyle, and current health concerns.",
      },
      {
        title: "Health Assessment",
        description:
          "Relevant health indicators and preventive requirements are professionally assessed.",
      },
      {
        title: "Prevention Plan",
        description:
          "A practical and personalized preventive healthcare plan is recommended.",
      },
    ],
  },
  {
    id: 3,
    slug: "health-checkup",
    title: "Health Checkup",
    category: "Routine Screening",
    shortDescription:
      "Structured routine health assessments that help patients understand and monitor their overall health.",
    description:
      "Regular health checkups help patients monitor important health indicators and identify concerns before they become more serious. Our approach focuses on clear communication, responsible screening guidance, and practical follow-up recommendations.",
    image: healthCheckupImage,
    icon: "03",
    duration: "30–45 minutes",
    availability: "Monday to Saturday",
    suitableFor: [
      "Adults requiring routine annual checkups",
      "Patients monitoring ongoing health indicators",
      "Individuals beginning a new wellness routine",
      "People seeking a general overview of their health",
    ],
    benefits: [
      "Better awareness of current health status",
      "Early identification of unusual health indicators",
      "Professional follow-up recommendations",
      "Support for long-term health monitoring",
    ],
    process: [
      {
        title: "Health History",
        description:
          "Relevant personal health information, symptoms, and previous reports are reviewed.",
      },
      {
        title: "Routine Evaluation",
        description:
          "Basic health indicators and applicable screening requirements are assessed.",
      },
      {
        title: "Results Guidance",
        description:
          "The doctor explains findings and recommends appropriate health actions.",
      },
    ],
  },
  {
    id: 4,
    slug: "diagnostic-support",
    title: "Diagnostic Support",
    category: "Clinical Assistance",
    shortDescription:
      "Guidance for understanding medical reports, recommended tests, and the next steps in your care.",
    description:
      "Diagnostic support helps patients understand recommended medical tests and existing reports. Our healthcare professionals explain relevant findings in clear language and guide patients toward appropriate follow-up care.",
    image: diagnosticSupportImage,
    icon: "04",
    duration: "20–30 minutes",
    availability: "Monday to Saturday",
    suitableFor: [
      "Patients with recent medical reports",
      "Individuals advised to complete diagnostic tests",
      "Patients requiring follow-up interpretation",
      "People seeking clarity about recommended investigations",
    ],
    benefits: [
      "Simple explanation of diagnostic information",
      "Guidance about relevant follow-up tests",
      "Better preparation for specialist consultation",
      "Clear direction for the next stage of care",
    ],
    process: [
      {
        title: "Report Review",
        description:
          "Available diagnostic reports, prescriptions, and medical history are reviewed.",
      },
      {
        title: "Clinical Explanation",
        description:
          "Important findings are explained clearly in a patient-friendly manner.",
      },
      {
        title: "Next-Step Guidance",
        description:
          "You receive practical advice regarding follow-up tests or consultations.",
      },
    ],
  },
  {
    id: 5,
    slug: "chronic-care",
    title: "Chronic Care",
    category: "Ongoing Support",
    shortDescription:
      "Continuous healthcare support for patients managing long-term medical conditions.",
    description:
      "Chronic care supports patients who require regular monitoring and responsible management of long-term health conditions. The focus is on consistent follow-up, medication awareness, lifestyle support, and improved patient understanding.",
    image: chronicCareImage,
    icon: "05",
    duration: "30–40 minutes",
    availability: "Monday to Friday",
    suitableFor: [
      "Patients managing diabetes",
      "Individuals monitoring high blood pressure",
      "Patients requiring regular health follow-up",
      "People managing long-term medical conditions",
    ],
    benefits: [
      "Structured and regular health monitoring",
      "Improved understanding of ongoing conditions",
      "Medication and lifestyle awareness",
      "Consistent follow-up and care coordination",
    ],
    process: [
      {
        title: "Condition Review",
        description:
          "The doctor reviews your condition, current treatment, symptoms, and recent reports.",
      },
      {
        title: "Progress Monitoring",
        description:
          "Health progress and important clinical indicators are regularly evaluated.",
      },
      {
        title: "Ongoing Care Plan",
        description:
          "A practical follow-up plan is created to support long-term condition management.",
      },
    ],
  },
  {
    id: 6,
    slug: "wellness-guidance",
    title: "Wellness Guidance",
    category: "Lifestyle Support",
    shortDescription:
      "Personalized guidance for healthier routines, improved well-being, and sustainable lifestyle habits.",
    description:
      "Our wellness guidance service helps patients make realistic and sustainable improvements in their everyday routines. Recommendations are based on individual health goals, lifestyle patterns, and personal requirements.",
    image: wellnessGuidanceImage,
    icon: "06",
    duration: "30 minutes",
    availability: "Tuesday to Saturday",
    suitableFor: [
      "Individuals beginning a healthier lifestyle",
      "People seeking improved sleep and daily routines",
      "Patients working toward practical wellness goals",
      "Individuals requiring general lifestyle guidance",
    ],
    benefits: [
      "Personalized and practical wellness planning",
      "Support for healthier everyday routines",
      "Improved awareness of lifestyle choices",
      "Realistic goals designed for long-term consistency",
    ],
    process: [
      {
        title: "Lifestyle Discussion",
        description:
          "Your routine, habits, health goals, and major wellness challenges are discussed.",
      },
      {
        title: "Goal Planning",
        description:
          "Realistic and achievable wellness priorities are identified.",
      },
      {
        title: "Personal Guidance",
        description:
          "You receive a practical plan for improving your daily health habits.",
      },
    ],
  },
];

export const serviceFeatures = [
  {
    id: 1,
    title: "Professional Consultation",
    description:
      "Every consultation follows a responsible and patient-focused approach.",
  },
  {
    id: 2,
    title: "Clear Communication",
    description:
      "Health guidance is explained in simple and understandable language.",
  },
  {
    id: 3,
    title: "Personalized Attention",
    description:
      "Recommendations are based on individual requirements and concerns.",
  },
  {
    id: 4,
    title: "Follow-Up Support",
    description:
      "Patients receive clear instructions regarding their next healthcare steps.",
  },
];

export default services;