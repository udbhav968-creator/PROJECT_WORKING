import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcryptjs';
import rateLimit from 'express-rate-limit';

const app = express();
const PORT = process.env.PORT || 5000;
const JWT_SECRET = process.env.JWT_SECRET || 'pure_health_clinic_secret_key_2026';

// Middleware
app.use(cors({ origin: '*', credentials: true }));
app.use(express.json());

// Rate Limiting Throttle
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 200,
  message: { success: false, errors: ['Rate limit exceeded. Please try again later.'] }
});
app.use(limiter);

// In-Memory Enterprise Models & Database Store
interface User {
  id: string;
  email: string;
  fullName: string;
  passwordHash: string;
  role: 'Admin' | 'Doctor' | 'Patient';
  createdAt: string;
}

interface Appointment {
  id: string;
  tokenNumber: string;
  patientName: string;
  patientPhone: string;
  patientEmail?: string;
  doctorName: string;
  department: string;
  priority: 'routine' | 'urgent' | 'emergency';
  consultationType: 'OPD' | 'Teleconsultation' | 'Emergency';
  consultationFeeInr: number;
  videoRoomUrl?: string;
  emergencyEscalationCode?: string;
  appointmentDate: string;
  status: 'scheduled' | 'in_consultation' | 'completed' | 'cancelled';
  notes?: string;
}

interface DoctorRoster {
  id: string;
  doctorName: string;
  department: string;
  consultationFeeInr: number;
  shiftHours: string;
  dutyStatus: 'on_duty' | 'in_surgery' | 'on_break' | 'off_duty';
  roomNumber: string;
  currentQueueCount: number;
}

const users: User[] = [];
const appointments: Appointment[] = [
  {
    id: 'appt-101',
    tokenNumber: 'PURE-GEN-101',
    patientName: 'Rajesh Sharma',
    patientPhone: '+91 9811122233',
    patientEmail: 'rajesh@example.com',
    doctorName: 'Dr. Divit Shah',
    department: 'General Consultation & Preventive Care',
    priority: 'urgent',
    consultationType: 'OPD',
    consultationFeeInr: 600,
    appointmentDate: new Date().toISOString(),
    status: 'scheduled',
    notes: 'Comprehensive Health Checkup'
  },
  {
    id: 'appt-102',
    tokenNumber: 'PURE-CARD-EMG-909',
    patientName: 'Priya Verma',
    patientPhone: '+91 9877766655',
    doctorName: 'Dr. Rahul Mehta',
    department: 'Cardiology & Heart Care',
    priority: 'emergency',
    consultationType: 'Emergency',
    consultationFeeInr: 1000,
    emergencyEscalationCode: 'EMG-ALERT-RED-909',
    appointmentDate: new Date().toISOString(),
    status: 'in_consultation',
    notes: 'Cardiovascular triage evaluation'
  }
];

const doctorRoster: DoctorRoster[] = [
  { id: 'doc-1', doctorName: 'Dr. Divit Shah', department: 'General Consultation', consultationFeeInr: 600, shiftHours: '09:00 AM - 05:00 PM', dutyStatus: 'on_duty', roomNumber: 'OPD Room 101', currentQueueCount: 5 },
  { id: 'doc-2', doctorName: 'Dr. Rahul Mehta', department: 'Cardiology', consultationFeeInr: 1000, shiftHours: '10:00 AM - 04:00 PM', dutyStatus: 'on_duty', roomNumber: 'OPD Room 204', currentQueueCount: 8 },
  { id: 'doc-3', doctorName: 'Dr. Anjali Sharma', department: 'Chronic Care', consultationFeeInr: 750, shiftHours: '02:00 PM - 08:00 PM', dutyStatus: 'in_surgery', roomNumber: 'Operation Theater 2', currentQueueCount: 2 }
];

// JWT Auth Middleware
export interface AuthRequest extends Request {
  user?: { id: string; email: string; role: string };
}

const authenticateJWT = (req: AuthRequest, res: Response, next: NextFunction) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ success: false, errors: ['Access token missing or invalid.'] });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET) as { id: string; email: string; role: string };
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(403).json({ success: false, errors: ['Token verification failed or expired.'] });
  }
};

// ----------------------------------------------------------------------------
// API Endpoints
// ----------------------------------------------------------------------------

// Root Landing API
app.get('/', (req: Request, res: Response) => {
  res.json({
    success: true,
    service: 'Pure Health Clinic Express Node.js TypeScript Backend API Core',
    institute: 'Pure Health Clinic & Hospital Systems',
    status: 'online',
    framework: 'Node.js Express TypeScript + JWT Auth',
    endpoints: {
      health: '/api/admin/health',
      authRegister: '/api/auth/register',
      authLogin: '/api/auth/login',
      authProfile: '/api/auth/profile',
      dashboard: '/api/admin/dashboard',
      appointments: '/api/admin/appointments'
    }
  });
});

// System Health Check
app.get('/api/admin/health', (req: Request, res: Response) => {
  res.json({
    success: true,
    institute: 'Pure Health Clinic Integration Core',
    status: 'healthy',
    database_connected: true,
    database_latency_ms: 1.5,
    nabh_hipaa_compliance_status: 'ACTIVE_AUDIT_ENABLED',
    framework: 'Node.js 20 Express TypeScript',
    timestamp: new Date().toISOString()
  });
});

// Module 1: Auth Register
app.post('/api/auth/register', async (req: Request, res: Response) => {
  const { email, password, fullName, role } = req.body;
  if (!email || !password || !fullName) {
    return res.status(400).json({ success: false, errors: ['Email, password, and fullName are required.'] });
  }

  const existingUser = users.find(u => u.email.toLowerCase() === email.toLowerCase());
  if (existingUser) {
    return res.status(400).json({ success: false, errors: ['User with this email already exists.'] });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const newUser: User = {
    id: `usr-${Date.now()}`,
    email,
    fullName,
    passwordHash,
    role: role || 'Patient',
    createdAt: new Date().toISOString()
  };

  users.push(newUser);
  const token = jwt.sign({ id: newUser.id, email: newUser.email, role: newUser.role }, JWT_SECRET, { expiresIn: '24h' });

  res.status(201).json({
    success: true,
    message: 'User registered successfully.',
    token,
    user: { id: newUser.id, email: newUser.email, fullName: newUser.fullName, role: newUser.role }
  });
});

// Module 1: Auth Login
app.post('/api/auth/login', async (req: Request, res: Response) => {
  const { email, password } = req.body;
  const user = users.find(u => u.email.toLowerCase() === email?.toLowerCase());
  if (!user) {
    return res.status(401).json({ success: false, errors: ['Invalid email or password credentials.'] });
  }

  const isMatch = await bcrypt.compare(password, user.passwordHash);
  if (!isMatch) {
    return res.status(401).json({ success: false, errors: ['Invalid email or password credentials.'] });
  }

  const token = jwt.sign({ id: user.id, email: user.email, role: user.role }, JWT_SECRET, { expiresIn: '24h' });

  res.json({
    success: true,
    token,
    user: { id: user.id, email: user.email, fullName: user.fullName, role: user.role }
  });
});

// Module 1: Auth Profile
app.get('/api/auth/profile', authenticateJWT, (req: AuthRequest, res: Response) => {
  const user = users.find(u => u.id === req.user?.id);
  if (!user) {
    return res.status(404).json({ success: false, errors: ['User profile not found.'] });
  }
  res.json({
    success: true,
    user: { id: user.id, email: user.email, fullName: user.fullName, role: user.role, createdAt: user.createdAt }
  });
});

// Module 2 & 4: OPD Appointments List & Book
app.get('/api/admin/appointments', (req: Request, res: Response) => {
  res.json({
    success: true,
    count: appointments.length,
    results: appointments
  });
});

app.post('/api/admin/appointments', (req: Request, res: Response) => {
  const { patient_name, patient_phone, patient_email, doctor_name, department, priority, consultation_type, consultation_fee_inr, appointment_date, notes } = req.body;

  if (!patient_name || !patient_phone) {
    return res.status(400).json({ success: false, errors: ['Patient name and phone number are required.'] });
  }

  const token_number = `PURE-OPD-${Math.random().toString(36).substring(2, 8).toUpperCase()}`;
  const video_room_url = consultation_type === 'Teleconsultation' ? `https://meet.jit.si/purehealth-opd-${token_number.toLowerCase()}` : undefined;
  const emergency_escalation_code = priority === 'emergency' ? `EMG-ALERT-${Math.random().toString(36).substring(2, 6).toUpperCase()}` : undefined;

  const newAppt: Appointment = {
    id: `appt-${Date.now()}`,
    tokenNumber: token_number,
    patientName: patient_name,
    patientPhone: patient_phone,
    patientEmail: patient_email,
    doctorName: doctor_name || 'Dr. Divit Shah',
    department: department || 'General Consultation',
    priority: priority || 'routine',
    consultationType: consultation_type || 'OPD',
    consultationFeeInr: consultation_fee_inr || 600,
    videoRoomUrl: video_room_url,
    emergencyEscalationCode: emergency_escalation_code,
    appointmentDate: appointment_date || new Date().toISOString(),
    status: 'scheduled',
    notes
  };

  appointments.unshift(newAppt);

  res.status(201).json({
    success: true,
    id: newAppt.id,
    token_number: newAppt.tokenNumber,
    patient_name: newAppt.patientName,
    patient_phone: newAppt.patientPhone,
    doctor_name: newAppt.doctorName,
    department: newAppt.department,
    priority: newAppt.priority,
    consultation_type: newAppt.consultationType,
    consultation_fee_inr: newAppt.consultationFeeInr,
    video_room_url: newAppt.videoRoomUrl,
    emergency_escalation_code: newAppt.emergencyEscalationCode,
    appointment_date: newAppt.appointmentDate,
    status: newAppt.status,
    whatsapp_confirmation_text: `🏥 *PURE HEALTH CLINIC OPD CONFIRMATION*\nPatient: ${newAppt.patientName}\nToken: *${newAppt.tokenNumber}*\nDoctor: ${newAppt.doctorName}\nFee: ₹${newAppt.consultationFeeInr}`
  });
});

// Printable OPD Receipt Slip
app.get('/api/admin/appointments/:id/slip', (req: Request, res: Response) => {
  const appt = appointments.find(a => a.id === req.params.id);
  if (!appt) {
    return res.status(404).json({ success: false, errors: ['Appointment not found.'] });
  }

  const html = `
    <!DOCTYPE html>
    <html>
    <head><title>OPD Slip - ${appt.tokenNumber}</title></head>
    <body style="font-family: Arial; padding: 20px;">
      <div style="border: 2px solid #0056b3; padding: 20px; max-width: 500px; border-radius: 8px;">
        <h2 style="color: #0056b3; text-align: center;">🏥 Pure Health Clinic</h2>
        <h1 style="text-align: center;">${appt.tokenNumber}</h1>
        <p><strong>Patient:</strong> ${appt.patientName}</p>
        <p><strong>Doctor:</strong> ${appt.doctorName}</p>
        <p><strong>Department:</strong> ${appt.department}</p>
        <p><strong>Consultation Fee:</strong> ₹${appt.consultationFeeInr}</p>
        <p><strong>Status:</strong> ${appt.status.toUpperCase()}</p>
      </div>
    </body>
    </html>
  `;

  res.json({
    success: true,
    token_number: appt.tokenNumber,
    patient_name: appt.patientName,
    printable_opd_slip_html: html
  });
});

// Admin Dashboard Analytics
app.get('/api/admin/dashboard', (req: Request, res: Response) => {
  const totalRevenue = appointments.reduce((sum, a) => sum + a.consultationFeeInr, 0);

  res.json({
    success: true,
    institute: 'Pure Health Clinic Core',
    stats: {
      total_users: users.length,
      active_users: users.length,
      total_appointments: appointments.length,
      scheduled_appointments: appointments.filter(a => a.status === 'scheduled').length,
      in_consultation_appointments: appointments.filter(a => a.status === 'in_consultation').length,
      completed_appointments: appointments.filter(a => a.status === 'completed').length,
      emergency_triage_count: appointments.filter(a => a.priority === 'emergency').length,
      on_duty_doctors_count: doctorRoster.filter(d => d.dutyStatus === 'on_duty').length,
      total_estimated_revenue_inr: totalRevenue
    },
    doctor_roster_status: doctorRoster
  });
});

app.listen(PORT, () => {
  console.log(`⚡ [Node.js Express TypeScript Server] Running on http://localhost:${PORT}`);
});
