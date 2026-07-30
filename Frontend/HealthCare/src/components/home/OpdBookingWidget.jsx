import React, { useState } from 'react';

const API_BASE_URL = window.location.origin.includes('localhost')
  ? 'http://127.0.0.1:8000/api/admin/appointments/'
  : '/api/admin/appointments/';

export default function OpdBookingWidget() {
  const [formData, setFormData] = useState({
    patient_name: '',
    patient_phone: '',
    patient_email: '',
    doctor_name: 'Dr. Divit Shah',
    department: 'General_Consultation',
    priority: 'routine',
    consultation_type: 'OPD',
    appointment_date: new Date().toISOString().slice(0, 16),
    notes: ''
  });

  const [loading, setLoading] = useState(false);
  const [bookingResult, setBookingResult] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage('');
    setBookingResult(null);

    try {
      const response = await fetch(API_BASE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          appointment_date: new Date(formData.appointment_date).toISOString()
        })
      });

      const data = await response.json();

      if (response.ok) {
        setBookingResult(data);
      } else {
        setErrorMessage(data.errors ? data.errors.join(', ') : 'Failed to book appointment. Please verify details.');
      }
    } catch (err) {
      setErrorMessage('Network error connecting to Pure Health Clinic API. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="opd-widget-card">
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <span className="triage-badge-red" style={{ background: '#0a2540', marginBottom: '8px', display: 'inline-block' }}>
          🏥 Pure Health OPD Booking Portal
        </span>
        <h2 style={{ fontSize: '1.8rem', color: '#0a2540' }}>Instant Clinical OPD Token & Tele-Health Scheduling</h2>
        <p style={{ color: '#64748b', fontSize: '0.95rem' }}>Auto-Generates Official Clinical OPD Tokens, Tele-Health Video Links & Emergency Triage Alerts</p>
      </div>

      {errorMessage && (
        <div style={{ background: '#fee2e2', color: '#991b1b', padding: '12px', borderRadius: '10px', marginBottom: '16px', fontSize: '0.9rem' }}>
          ⚠️ {errorMessage}
        </div>
      )}

      {!bookingResult ? (
        <form onSubmit={handleSubmit}>
          <div className="input-group-grid">
            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Patient Full Name *</label>
              <input
                type="text"
                name="patient_name"
                required
                placeholder="e.g. Rajesh Sharma"
                value={formData.patient_name}
                onChange={handleChange}
                className="custom-form-input"
              />
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Patient Mobile Number *</label>
              <input
                type="tel"
                name="patient_phone"
                required
                placeholder="e.g. +91 9811122233"
                value={formData.patient_phone}
                onChange={handleChange}
                className="custom-form-input"
              />
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Select Clinical Department *</label>
              <select name="department" value={formData.department} onChange={handleChange} className="custom-form-select">
                <option value="General_Consultation">General Consultation & Preventive Care</option>
                <option value="Cardiology">Cardiology & Heart Care (Dr. Rahul Mehta)</option>
                <option value="Chronic_Care">Chronic Disease Care (Dr. Anjali Sharma)</option>
                <option value="Diagnostic_Support">Diagnostic & Lab Support</option>
                <option value="Wellness_Guidance">Wellness & Lifestyle Guidance</option>
                <option value="Emergency_Care">Emergency & Urgent Triage</option>
              </select>
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Attending Specialist Doctor *</label>
              <select name="doctor_name" value={formData.doctor_name} onChange={handleChange} className="custom-form-select">
                <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Senior Cardiologist - ₹1000)</option>
                <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                <option value="Dr. Ayesha Khan">Dr. Ayesha Khan (Pediatrics - ₹500)</option>
              </select>
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Consultation Priority / Triage *</label>
              <select name="priority" value={formData.priority} onChange={handleChange} className="custom-form-select">
                <option value="routine">Routine OPD Visit</option>
                <option value="urgent">Urgent Priority Referral</option>
                <option value="emergency">🚨 Emergency Triage (Instant Red Alert)</option>
              </select>
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Mode of Consultation *</label>
              <select name="consultation_type" value={formData.consultation_type} onChange={handleChange} className="custom-form-select">
                <option value="OPD">Outpatient Department (OPD Visit)</option>
                <option value="Teleconsultation">📹 Tele-Health Video Consultation</option>
                <option value="Emergency">🚨 Emergency ER Visit</option>
              </select>
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Appointment Date & Time *</label>
              <input
                type="datetime-local"
                name="appointment_date"
                required
                value={formData.appointment_date}
                onChange={handleChange}
                className="custom-form-input"
              />
            </div>

            <div>
              <label style={{ fontWeight: 600, fontSize: '0.85rem', color: '#334155' }}>Patient Medical Notes</label>
              <input
                type="text"
                name="notes"
                placeholder="Brief symptoms or health concerns"
                value={formData.notes}
                onChange={handleChange}
                className="custom-form-input"
              />
            </div>
          </div>

          <div style={{ marginTop: '24px' }}>
            <button type="submit" disabled={loading} className="btn-book-opd">
              {loading ? '⏳ Generating OPD Token & Booking...' : '🎟️ Book OPD Appointment & Generate Token'}
            </button>
          </div>
        </form>
      ) : (
        <div className="token-receipt-modal">
          <div style={{ textAlign: 'center', marginBottom: '16px' }}>
            <span style={{ background: '#dcfce7', color: '#15803d', padding: '6px 16px', borderRadius: '20px', fontWeight: '700', fontSize: '0.85rem' }}>
              ✅ OPD APPOINTMENT BOOKED SUCCESSFULLY
            </span>
          </div>

          <div className="receipt-token-number">{bookingResult.token_number}</div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', marginTop: '16px', fontSize: '0.92rem' }}>
            <div><strong>Patient:</strong> {bookingResult.patient_name}</div>
            <div><strong>Phone:</strong> {bookingResult.patient_phone}</div>
            <div><strong>Doctor:</strong> {bookingResult.doctor_name}</div>
            <div><strong>Department:</strong> {bookingResult.department}</div>
            <div><strong>Consultation Fee:</strong> ₹{bookingResult.consultation_fee_inr}</div>
            <div><strong>Priority:</strong> <span style={{ textTransform: 'uppercase', fontWeight: 700 }}>{bookingResult.priority}</span></div>
          </div>

          {bookingResult.video_room_url && (
            <div style={{ background: '#e0f2fe', padding: '12px', borderRadius: '10px', marginTop: '16px', textAlign: 'center' }}>
              📹 <strong>Tele-Consultation Room Link:</strong><br />
              <a href={bookingResult.video_room_url} target="_blank" rel="noopener noreferrer" style={{ color: '#0284c7', fontWeight: 700, wordBreak: 'break-all' }}>
                {bookingResult.video_room_url}
              </a>
            </div>
          )}

          {bookingResult.emergency_escalation_code && (
            <div style={{ background: '#fee2e2', color: '#b91c1c', padding: '12px', borderRadius: '10px', marginTop: '16px', textAlign: 'center', fontWeight: 700 }}>
              🚨 EMERGENCY ALERT CODE: {bookingResult.emergency_escalation_code}
            </div>
          )}

          <div style={{ marginTop: '20px', display: 'flex', gap: '12px' }}>
            <button
              onClick={() => window.open(`/api/admin/appointments/${bookingResult.id}/slip/`, '_blank')}
              style={{ flex: 1, padding: '12px', background: '#0a2540', color: '#fff', border: 'none', borderRadius: '10px', fontWeight: 700, cursor: 'pointer' }}
            >
              🖨️ Print Reception OPD Slip
            </button>
            <button
              onClick={() => setBookingResult(null)}
              style={{ padding: '12px 24px', background: '#e2e8f0', color: '#334155', border: 'none', borderRadius: '10px', fontWeight: 700, cursor: 'pointer' }}
            >
              Book Another OPD
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
