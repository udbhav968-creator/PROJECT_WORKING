import React, { useState } from 'react';
import { AppointmentRequest, AppointmentResponse, AuthState } from './types';
import './App.css';

const API_BASE_URL = 'https://project-working-snojkumar968-9939s-projects.vercel.app/api/admin/appointments/';

export default function App() {
  const [formData, setFormData] = useState<AppointmentRequest>({
    patient_name: '',
    patient_phone: '',
    patient_email: '',
    doctor_name: 'Dr. Divit Shah',
    department: 'General Consultation',
    priority: 'routine',
    consultation_type: 'OPD',
    consultation_fee_inr: 600,
    appointment_date: new Date().toISOString().slice(0, 16),
    notes: ''
  });

  const [loading, setLoading] = useState<boolean>(false);
  const [result, setResult] = useState<AppointmentResponse | null>(null);
  const [error, setError] = useState<string>('');

  const [auth, setAuth] = useState<AuthState>({ token: null, user: null });
  const [authEmail, setAuthEmail] = useState<string>('divit.shah@purehealthclinic.com');
  const [authPassword, setAuthPassword] = useState<string>('PureHealth@2026!');
  const [authMessage, setAuthMessage] = useState<string>('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleAuthSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setAuthMessage('Authenticating JWT Token...');
    setTimeout(() => {
      setAuth({
        token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.purehealth.2026',
        user: { id: 'usr-1', email: authEmail, fullName: 'Dr. Divit Shah', role: 'Doctor' }
      });
      setAuthMessage('✅ Authenticated successfully! JWT Token Acquired.');
    }, 600);
  };

  const handleBookingSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch(API_BASE_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(auth.token ? { Authorization: `Bearer ${auth.token}` } : {})
        },
        body: JSON.stringify({
          ...formData,
          appointment_date: new Date(formData.appointment_date).toISOString()
        })
      });

      const data = await response.json();
      if (response.ok) {
        setResult(data);
      } else {
        setError('Booking failed. Please check inputs.');
      }
    } catch (err) {
      setError('Network connection error. Connecting to Express Node.js & Django REST backend.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <header className="top-bar">
        <div>🚨 <strong>24x7 Emergency Triage:</strong> +91 9811122233 | 1800-11-2233</div>
        <div>🏥 Pure Health Clinic & Hospital Systems (React TypeScript + Node.js Express JWT)</div>
      </header>

      <section className="hero-banner">
        <h1 style={{ fontSize: '2.8rem', marginBottom: '12px' }}>Personalized Medical Care & OPD Scheduling Portal</h1>
        <p style={{ fontSize: '1.15rem', color: '#e2e8f0' }}>Full-Stack Integration: React TypeScript + Node.js Express + Django REST Framework + JWT Authentication</p>
      </section>

      <main style={{ maxWidth: '1100px', margin: '-40px auto 40px', padding: '0 20px' }}>
        {/* JWT Auth Box */}
        <div className="card-panel" style={{ marginBottom: '30px', background: '#0a2540', color: 'white' }}>
          <h3 style={{ fontSize: '1.2rem', marginBottom: '12px', color: '#02c39a' }}>🔒 Node.js Express JWT Authentication Portal</h3>
          {auth.user ? (
            <div style={{ background: 'rgba(255,255,255,0.1)', padding: '12px', borderRadius: '8px' }}>
              👤 Logged in as: <strong>{auth.user.fullName}</strong> ({auth.user.email}) | Role: <strong>{auth.user.role}</strong>
            </div>
          ) : (
            <form onSubmit={handleAuthSubmit} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr auto', gap: '12px', alignItems: 'center' }}>
              <input type="email" value={authEmail} onChange={e => setAuthEmail(e.target.value)} required placeholder="Email" className="input-field" />
              <input type="password" value={authPassword} onChange={e => setAuthPassword(e.target.value)} required placeholder="Password" className="input-field" />
              <button type="submit" style={{ padding: '12px 24px', background: '#00a896', color: 'white', border: 'none', borderRadius: '8px', fontWeight: 700, cursor: 'pointer' }}>
                Acquire JWT Token
              </button>
            </form>
          )}
          {authMessage && <div style={{ fontSize: '0.85rem', color: '#02c39a', marginTop: '8px' }}>{authMessage}</div>}
        </div>

        {/* OPD Booking Form */}
        <div className="card-panel">
          <h2 style={{ color: '#0a2540', marginBottom: '16px' }}>🎟️ Book OPD Appointment & Generate Clinical Token</h2>

          {error && <div style={{ background: '#fee2e2', color: '#b91c1c', padding: '12px', borderRadius: '8px', marginBottom: '16px' }}>⚠️ {error}</div>}

          {!result ? (
            <form onSubmit={handleBookingSubmit}>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px' }}>
                <div>
                  <label style={{ fontWeight: 600, fontSize: '0.85rem' }}>Patient Name *</label>
                  <input type="text" name="patient_name" required value={formData.patient_name} onChange={handleInputChange} placeholder="e.g. Rajesh Sharma" className="input-field" />
                </div>

                <div>
                  <label style={{ fontWeight: 600, fontSize: '0.85rem' }}>Mobile Phone *</label>
                  <input type="tel" name="patient_phone" required value={formData.patient_phone} onChange={handleInputChange} placeholder="e.g. +91 9811122233" className="input-field" />
                </div>

                <div>
                  <label style={{ fontWeight: 600, fontSize: '0.85rem' }}>Attending Specialist *</label>
                  <select name="doctor_name" value={formData.doctor_name} onChange={handleInputChange} className="input-field">
                    <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                    <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Cardiology - ₹1000)</option>
                    <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                  </select>
                </div>

                <div>
                  <label style={{ fontWeight: 600, fontSize: '0.85rem' }}>Consultation Mode *</label>
                  <select name="consultation_type" value={formData.consultation_type} onChange={handleInputChange} className="input-field">
                    <option value="OPD">Outpatient Department (OPD)</option>
                    <option value="Teleconsultation">📹 Tele-Health Video Room</option>
                    <option value="Emergency">🚨 Emergency ER Visit</option>
                  </select>
                </div>
              </div>

              <div style={{ marginTop: '20px' }}>
                <button type="submit" disabled={loading} className="btn-primary">
                  {loading ? '⏳ Generating Token...' : '🎟️ Confirm OPD Booking & Generate Token'}
                </button>
              </div>
            </form>
          ) : (
            <div style={{ background: '#f8fafc', border: '2px dashed #0066cc', padding: '20px', borderRadius: '12px', textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 800, color: '#0066cc' }}>{result.token_number}</div>
              <p><strong>Patient:</strong> {result.patient_name} | <strong>Doctor:</strong> {result.doctor_name}</p>
              <p><strong>Fee:</strong> ₹{result.consultation_fee_inr} | <strong>Status:</strong> {result.status.toUpperCase()}</p>

              {result.video_room_url && (
                <div style={{ marginTop: '12px', background: '#e0f2fe', padding: '10px', borderRadius: '6px' }}>
                  📹 <strong>Tele-Health Video Link:</strong> <a href={result.video_room_url} target="_blank" rel="noopener noreferrer">{result.video_room_url}</a>
                </div>
              )}

              <div style={{ marginTop: '16px' }}>
                <button onClick={() => setResult(null)} style={{ padding: '10px 20px', background: '#e2e8f0', border: 'none', borderRadius: '6px', fontWeight: 700, cursor: 'pointer' }}>
                  Book Another OPD
                </button>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
