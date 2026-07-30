export interface AppointmentRequest {
  patient_name: string;
  patient_phone: string;
  patient_email?: string;
  doctor_name: string;
  department: string;
  priority: 'routine' | 'urgent' | 'emergency';
  consultation_type: 'OPD' | 'Teleconsultation' | 'Emergency';
  consultation_fee_inr: number;
  appointment_date: string;
  notes?: string;
}

export interface AppointmentResponse {
  success: boolean;
  id: string;
  token_number: string;
  patient_name: string;
  patient_phone: string;
  doctor_name: string;
  department: string;
  priority: string;
  consultation_type: string;
  consultation_fee_inr: number;
  video_room_url?: string;
  emergency_escalation_code?: string;
  appointment_date: string;
  status: string;
  whatsapp_confirmation_text?: string;
}

export interface DoctorRosterItem {
  id: string;
  doctorName: string;
  department: string;
  consultationFeeInr: number;
  shiftHours: string;
  dutyStatus: 'on_duty' | 'in_surgery' | 'on_break' | 'off_duty';
  roomNumber: string;
  currentQueueCount: number;
}

export interface AuthUser {
  id: string;
  email: string;
  fullName: string;
  role: 'Admin' | 'Doctor' | 'Patient';
}

export interface AuthState {
  token: string | null;
  user: AuthUser | null;
}
